from app.config import generate_id
from app.models.user import User
from app.models.book import Book


class Order:
    def __init__(self, user: User, book: Book):
        self._id = generate_id()
        self._user = user
        self._book = book

    def get_id(self) -> str:
        return self._id

    def get_user(self) -> User:
        return self._user

    def get_book(self) -> Book:
        return self._book
