import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from unittest.mock import Mock
from src.library import Library

class LibraryMockTestCase(unittest.TestCase):
    def setUp(self):
        self.mock_repo = Mock(spec=["add_book", "remove_book", "get_all_books"])
        self.library = Library(self.mock_repo)

    def test_borrow_calls_remove_book(self):
        self.mock_repo.remove_book.return_value = True
        result = self.library.borrow_book("Wiedźmin")
        self.assertTrue(result)
        self.mock_repo.remove_book.assert_called_once_with("Wiedźmin")

        self.mock_repo.remove_book.reset_mock()
        self.mock_repo.remove_book.return_value = False
        result2 = self.library.borrow_book("Nieistniejąca Książka")
        self.assertFalse(result2)
        self.mock_repo.remove_book.assert_called_once_with("Nieistniejąca Książka")

    def test_return_calls_add_book(self):
        self.library.return_book("1984", "George Orwell", 1949)
        self.mock_repo.add_book.assert_called_once_with("1984", "George Orwell", 1949)

    def test_list_books_calls_get_all_books(self):
        sample = [("Tytuł", "Autor", 2000)]
        self.mock_repo.get_all_books.return_value = sample
        result = self.library.list_books()
        self.assertIs(result, sample)
        self.mock_repo.get_all_books.assert_called_once_with()

if __name__ == '__main__':
    unittest.main()
