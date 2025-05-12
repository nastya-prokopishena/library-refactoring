class Book:
    def __init__(self, title: str, author: str, year: int):
        self._title = title
        self._author = author
        self._year = year

    def get_title(self) -> str:
        pass

    def get_author(self) -> str:
        pass

    def get_year(self) -> int:
        pass