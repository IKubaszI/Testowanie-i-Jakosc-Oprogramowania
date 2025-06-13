import unittest
from src.lottery import Lottery

class TestLottery(unittest.TestCase):
    def test_find_repeated_sets_2(self):
        list = [1, 1, 3, 2, 2, 2, 4, 5]
        number = 2

        self.assertEqual(Lottery(list).find_repeated_sets(number), [1])

    def test_find_repeated_sets_3(self):
        list = [1, 1, 3, 2, 2, 2, 4, 5]
        number = 3

        self.assertEqual(Lottery(list).find_repeated_sets(number), [2])

    def test_find_repeated_sets_2_find_2_numbers(self):
        self.assertEqual(Lottery([1, 2, 2, 2, 3, 4, 5, 5, 1]).find_repeated_sets(2), [1, 5])

    def test_find_repeated_sets_None_list(self):
        list = None
        number = 1

        self.assertEqual(Lottery(list).find_repeated_sets(number), [])

    def test_find_repeated_sets_None_number(self):
        list = [1, 2, 3]
        number = None

        self.assertEqual(Lottery(list).find_repeated_sets(number), [])

    def test_find_repeated_sets_full_None(self):
        list = None
        number = None

        self.assertEqual(Lottery(list).find_repeated_sets(number), [])

    def test_find_repeated_sets_empty_number_in_list(self):
        list = [1, 1, 2, 2, 2, 3, 4, 5]
        number = 7

        self.assertEqual(Lottery(list).find_repeated_sets(number), [])


if __name__ == '__main__':
    unittest.main()