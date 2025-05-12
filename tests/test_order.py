import unittest
from app.models import Order, User, Book


class TestOrder(unittest.TestCase):
    def setUp(self):
        self.user = User("Alice", "alice@example.com", "password123")
        self.book = Book("1984", "George Orwell", 1949)
        self.order = Order(self.user, self.book)

    def test_get_id(self):
        self.assertIsInstance(self.order.get_id(), str)

    def test_get_user(self):
        self.assertEqual(self.order.get_user(), self.user)

    def test_get_book(self):
        self.assertEqual(self.order.get_book(), self.book)


if __name__ == "__main__":
    unittest.main()
