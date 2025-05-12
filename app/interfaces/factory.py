from app.models.book import Book
from app.models.user import User


class Factory:
    @staticmethod
    def create_book(title: str, author: str, year: int) -> Book:
        return Book(title, author, year)

    @staticmethod
    def create_user(name: str, email: str, password: str) -> User:
        return User(name, email, password)
