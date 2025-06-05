from abc import ABC, abstractmethod

class LibraryRepository(ABC):
    @abstractmethod
    def add_book(self, title: str, author: str, year: int): pass

    @abstractmethod
    def remove_book(self, title: str) -> bool: pass

    @abstractmethod
    def get_all_books(self) -> list: pass
