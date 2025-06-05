import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from src.library import Library
from src.in_memory_repository import InMemoryRepository

class LibraryIntegrationTestCase(unittest.TestCase):
    def setUp(self):
        self.repo = InMemoryRepository()
        self.library = Library(self.repo)
        self.repo.add_book("Kubuś Puchatek", "A. A. Milne", 1926)
        self.repo.add_book("Mały Książę", "Antoine de Saint-Exupéry", 1943)

    def test_list_books_returns_all(self):
        books = self.library.list_books()
        expected = [
            ("Kubuś Puchatek", "A. A. Milne", 1926),
            ("Mały Książę", "Antoine de Saint-Exupéry", 1943)
        ]
        self.assertCountEqual(books, expected)

    def test_borrow_existing_book(self):
        result = self.library.borrow_book("Kubuś Puchatek")
        self.assertTrue(result)
        remaining = self.library.list_books()
        self.assertNotIn(("Kubuś Puchatek", "A. A. Milne", 1926), remaining)

    def test_borrow_nonexistent_book(self):
        result = self.library.borrow_book("Nieznana Książka")
        self.assertFalse(result)
        books = self.library.list_books()
        expected = [
            ("Kubuś Puchatek", "A. A. Milne", 1926),
            ("Mały Książę", "Antoine de Saint-Exupéry", 1943)
        ]
        self.assertCountEqual(books, expected)

    def test_return_book_adds_it(self):
        self.library.borrow_book("Mały Książę")
        self.assertNotIn(("Mały Książę", "Antoine de Saint-Exupéry", 1943), self.library.list_books())
        self.library.return_book("Mały Książę", "Antoine de Saint-Exupéry", 1943)
        books_after = self.library.list_books()
        self.assertIn(("Mały Książę", "Antoine de Saint-Exupéry", 1943), books_after)

if __name__ == '__main__':
    unittest.main()
