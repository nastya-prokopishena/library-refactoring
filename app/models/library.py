from typing import List, Optional

class Library:
    def __init__(self):
        self._books: List['Book'] = []

    def add_book(self, book: 'Book') -> None:
        pass

    def get_book(self, title: str) -> Optional['Book']:
        pass

    def get_all_books(self) -> List['Book']:
        pass
