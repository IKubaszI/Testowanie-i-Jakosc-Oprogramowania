import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from src.repeating import find_repeating_elements

class RepeatingElementsTestCase(unittest.TestCase):
    def test_single_repeating(self):
        nums = [1, 2, 2, 3, 3, 3]
        self.assertEqual(find_repeating_elements(nums, 2), [2])

    def test_multiple_repeating(self):
        nums = [4, 4, 5, 5, 5, 6, 6]
        self.assertCountEqual(find_repeating_elements(nums, 2), [4, 6])

    def test_exact_once(self):
        nums = [7, 8, 9]
        self.assertEqual(find_repeating_elements(nums, 1), [7, 8, 9])

    def test_none_matching(self):
        nums = [10, 10, 11, 11, 11]
        self.assertEqual(find_repeating_elements(nums, 3), [11])
        self.assertEqual(find_repeating_elements(nums, 2), [10])

    def test_empty_list(self):
        self.assertEqual(find_repeating_elements([], 1), [])

if __name__ == '__main__':
    unittest.main()
