import unittest
from app.models import Book


class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book("1984", "George Orwell", 1949)

    def test_get_title(self):
        self.assertEqual(self.book.get_title(), "1984")

    def test_get_author(self):
        self.assertEqual(self.book.get_author(), "George Orwell")

    def test_get_year(self):
        self.assertEqual(self.book.get_year(), 1949)


if __name__ == "__main__":
    unittest.main()
