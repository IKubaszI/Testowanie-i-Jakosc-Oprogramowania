from src.library_repository import LibraryRepository

class InMemoryRepository(LibraryRepository):
    def __init__(self):
        self._storage = {}

    def add_book(self, title: str, author: str, year: int):
        self._storage[title] = (author, year)

    def remove_book(self, title: str) -> bool:
        if title in self._storage:
            del self._storage[title]
            return True
        return False

    def get_all_books(self) -> list:
        return [(t, a, y) for t, (a, y) in self._storage.items()]
