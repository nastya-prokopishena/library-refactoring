import unittest
from app.models import Library, Book


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book = Book("1984", "George Orwell", 1949)

    def test_add_book(self):
        self.library.add_book(self.book)
        self.assertIn(self.book, self.library.get_all_books())

    def test_get_book_found(self):
        self.library.add_book(self.book)
        found_book = self.library.get_book("1984")
        self.assertEqual(found_book, self.book)


if __name__ == "__main__":
    unittest.main()
