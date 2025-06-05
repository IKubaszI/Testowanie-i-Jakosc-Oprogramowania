import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from src.lunar_vehicle import LunarVehicle

class LunarVehicleTestCase(unittest.TestCase):
    def test_initial_position(self):
        v = LunarVehicle(0, 0, 'N')
        self.assertEqual(v.get_position(), (0, 0, 'N'))

    def test_move_north(self):
        v = LunarVehicle(0, 0, 'N')
        v.move()
        self.assertEqual(v.get_position(), (0, 1, 'N'))

    def test_move_south(self):
        v = LunarVehicle(0, 0, 'S')
        v.move()
        self.assertEqual(v.get_position(), (0, -1, 'S'))

    def test_move_east(self):
        v = LunarVehicle(0, 0, 'E')
        v.move()
        self.assertEqual(v.get_position(), (1, 0, 'E'))

    def test_move_west(self):
        v = LunarVehicle(0, 0, 'W')
        v.move()
        self.assertEqual(v.get_position(), (-1, 0, 'W'))

    def test_turn_left(self):
        v = LunarVehicle(0, 0, 'N')
        v.turn_left()
        self.assertEqual(v.get_position(), (0, 0, 'W'))
        v.turn_left()
        self.assertEqual(v.get_position(), (0, 0, 'S'))

    def test_turn_right(self):
        v = LunarVehicle(0, 0, 'N')
        v.turn_right()
        self.assertEqual(v.get_position(), (0, 0, 'E'))
        v.turn_right()
        self.assertEqual(v.get_position(), (0, 0, 'S'))

    def test_execute_sequence(self):
        v = LunarVehicle(1, 2, 'N')
        v.execute("LMLMLMLMM")
        self.assertEqual(v.get_position(), (1, 3, 'N'))
        v2 = LunarVehicle(3, 3, 'E')
        v2.execute("MMRMMRMRRM")
        self.assertEqual(v2.get_position(), (5, 1, 'E'))

if __name__ == '__main__':
    unittest.main()
