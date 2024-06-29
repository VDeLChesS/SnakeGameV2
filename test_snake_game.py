import unittest
from main import update_snake_position, check_collisions, grow_snake


class TestSnakeGame(unittest.TestCase):

    def test_update_snake_position(self):
        snake_position = [100, 50]
        update_snake_position(snake_position, 'UP')
        self.assertEqual(snake_position, [100, 40])

        update_snake_position(snake_position, 'DOWN')
        self.assertEqual(snake_position, [100, 50])

        update_snake_position(snake_position, 'LEFT')
        self.assertEqual(snake_position, [90, 50])

        update_snake_position(snake_position, 'RIGHT')
        self.assertEqual(snake_position, [100, 50])

    def test_check_collisions(self):
        snake_position = [100, 50]
        snake_body = [[100, 50], [90, 50], [80, 50]]
        obstacles = [[200, 200], [300, 300]]
        self.assertFalse(check_collisions(snake_position, snake_body, 720, 480, obstacles))

        snake_position = [720, 50]
        self.assertTrue(check_collisions(snake_position, snake_body, 720, 480, obstacles))

        snake_position = [100, 480]
        self.assertTrue(check_collisions(snake_position, snake_body, 720, 480, obstacles))

        snake_position = [100, 50]
        snake_body = [[100, 50], [90, 50], [80, 50], [100, 50]]
        self.assertTrue(check_collisions(snake_position, snake_body, 720, 480, obstacles))

        snake_position = [200, 200]
        self.assertTrue(check_collisions(snake_position, snake_body, 720, 480, obstacles))

    def test_grow_snake(self):
        snake_body = [[100, 50], [90, 50], [80, 50]]
        snake_position = [110, 50]
        self.assertTrue(grow_snake(snake_body, True, snake_position))
        self.assertEqual(snake_body, [[110, 50], [100, 50], [90, 50], [80, 50]])

        snake_position = [120, 50]
        self.assertFalse(grow_snake(snake_body, False, snake_position))
        self.assertEqual(snake_body, [[120, 50], [110, 50], [100, 50], [90, 50]])


if __name__ == "__main__":
    unittest.main()

