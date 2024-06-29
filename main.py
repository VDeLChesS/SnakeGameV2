# snake_game.py

import pygame
import time
import random
from typing import List, Tuple

# Step 1: Setup the Development Environment
# Make sure you have Python and pygame installed:
# pip install pygame

# Step 2: Initialize Pygame
pygame.init()

# Step 3: Create the Game Window
window_x = 720
window_y = 480
game_window = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption('Snake Game')

# Step 4: Define Colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
grey = pygame.Color(169, 169, 169)

# Step 5: Set Up the Game Clock
fps = pygame.time.Clock()

# Step 6: Define the Snake
snake_speed = 15
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]

# Step 7: Define the Food
food_position = [random.randrange(1, (window_x // 10)) * 10,
                 random.randrange(1, (window_y // 10)) * 10]
food_spawn = True

# Define Obstacles
obstacles = [[random.randrange(1, (window_x // 10)) * 10,
              random.randrange(1, (window_y // 10)) * 10] for _ in range(2)]

# Load Sound Effects
pygame.mixer.init()
eat_sound = pygame.mixer.Sound('eat.wav')
game_over_sound = pygame.mixer.Sound('game_over.wav')

# Step 8: Handle User Input
direction = 'RIGHT'
change_to = direction
pause = False

# Step 9: Update the Snake's Position
def update_snake_position(snake_position: List[int], direction: str) -> None:
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

# Step 10: Check for Collisions
def check_collisions(snake_position: List[int], snake_body: List[List[int]], window_x: int, window_y: int, obstacles: List[List[int]]) -> bool:
    if snake_position[0] < 0 or snake_position[0] >= window_x:
        return True
    if snake_position[1] < 0 or snake_position[1] >= window_y:
        return True
    for block in snake_body[1:]:
        if snake_position == block:
            return True
    for obstacle in obstacles:
        if snake_position == obstacle:
            return True
    return False

# Step 11: Grow the Snake
def grow_snake(snake_body: List[List[int]], food_spawn: bool, snake_position: List[int]) -> bool:
    snake_body.insert(0, list(snake_position))
    if snake_position == food_position:
        pygame.mixer.Sound.play(eat_sound)
        return True
    else:
        snake_body.pop()
        return False

# Step 12: Draw Everything
def draw_elements(game_window: pygame.Surface, snake_body: List[List[int]], food_position: List[int], obstacles: List[List[int]]) -> None:
    game_window.fill(black)
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(food_position[0], food_position[1], 10, 10))
    for pos in obstacles:
        pygame.draw.rect(game_window, grey, pygame.Rect(pos[0], pos[1], 10, 10))

# Step 13: Update the Display
def update_display() -> None:
    pygame.display.flip()

# Step 14: Game Over Logic
def game_over() -> None:
    pygame.mixer.Sound.play(game_over_sound)
    font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = font.render('Your Score is : ' + str(len(snake_body) - 3), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x / 2, window_y / 4)
    game_window.fill(black)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    quit()

# Step 15: Pause the Game
def pause_game() -> None:
    paused = True
    font = pygame.font.SysFont('times new roman', 50)
    pause_surface = font.render('Paused', True, blue)
    pause_rect = pause_surface.get_rect()
    pause_rect.midtop = (window_x / 2, window_y / 4)
    game_window.blit(pause_surface, pause_rect)
    pygame.display.flip()
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = False

# Step 16: Main Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if direction != 'DOWN':
                    direction = 'UP'
            elif event.key == pygame.K_DOWN:
                if direction != 'UP':
                    direction = 'DOWN'
            elif event.key == pygame.K_LEFT:
                if direction != 'RIGHT':
                    direction = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                if direction != 'LEFT':
                    direction = 'RIGHT'
            elif event.key == pygame.K_p:
                pause_game()
            elif event.key == pygame.K_r:
                snake_position = [100, 50]
                snake_body = [[100, 50], [90, 50], [80, 50]]
                direction = 'RIGHT'
                food_position = [random.randrange(1, (window_x // 10)) * 10,
                                 random.randrange(1, (window_y // 10)) * 10]
                food_spawn = True
                obstacles = [[random.randrange(1, (window_x // 10)) * 10,
                              random.randrange(1, (window_y // 10)) * 10] for _ in range(5)]

    if not pause:
        update_snake_position(snake_position, direction)
        if check_collisions(snake_position, snake_body, window_x, window_y, obstacles):
            game_over()

        if grow_snake(snake_body, food_spawn, snake_position):
            food_spawn = False
        else:
            food_spawn = True

        if not food_spawn:
            food_position = [random.randrange(1, (window_x // 10)) * 10,
                             random.randrange(1, (window_y // 10)) * 10]

        draw_elements(game_window, snake_body, food_position, obstacles)
        update_display()
        fps.tick(snake_speed)

if __name__ == "__main__":
    main_menu()
    game_loop()