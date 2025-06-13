import unittest
from src.lunar import LunarRover
class TestLunarRover(unittest.TestCase):
    def setUp(self):
        self.rover = LunarRover()

    def test_initial_position(self):
        self.assertEqual(self.rover.get_position(), (0, 0))
        self.assertEqual(self.rover.get_direction(), 'N')

    def test_forward_movement(self):
        self.rover.move_forward(3)
        self.assertEqual(self.rover.get_position(), (0, 3))

    def test_backward_movement(self):
        self.rover.move_backward(2)
        self.assertEqual(self.rover.get_position(), (0, -2))

    def test_rotation_right(self):
        self.rover.rotate_right()
        self.assertEqual(self.rover.get_direction(), 'E')

    def test_rotation_left(self):
        self.rover.rotate_left()
        self.assertEqual(self.rover.get_direction(), 'W')

    def test_full_rotation(self):
        for _ in range(4):
            self.rover.rotate_right()
        self.assertEqual(self.rover.get_direction(), 'N')

    def test_combined_movement(self):
        self.rover.rotate_right()      # E
        self.rover.move_forward(5)     # x: +5
        self.rover.rotate_left()       # N
        self.rover.move_forward(2)     # y: +2
        self.assertEqual(self.rover.get_position(), (5, 2))
        self.assertEqual(self.rover.get_direction(), 'N')

    def test_invalid_direction_raises(self):
        with self.assertRaises(ValueError):
            LunarRover(start_direction='X')

if __name__ == '__main__':
    unittest.main()
