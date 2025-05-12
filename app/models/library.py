from typing import List, Optional

class Library:
    def __init__(self):
        self._books: List['Book'] = []

    def add_book(self, book: 'Book') -> None:
        self._books.append(book)

    def get_book(self, title: str) -> Optional['Book']:
        for book in self._books:
            if book.get_title() == title:
                return book
        return None

    def get_all_books(self) -> List['Book']:
        return self._books
