import unittest
from app.models import Order, User, Book
from datetime import datetime


class TestOrder(unittest.TestCase):
    def setUp(self):
        self.user = User("1", "Alice", "alice@example.com", "password123")
        self.book = Book("1984", "George Orwell", 1949)
        self.order = Order("order123", self.user, self.book)

    def test_get_order_id(self):
        self.assertEqual(self.order.get_order_id(), "order123")

    def test_get_user(self):
        self.assertEqual(self.order.get_user(), self.user)

    def test_get_book(self):
        self.assertEqual(self.order.get_book(), self.book)

    def test_get_created_at(self):
        created_at = self.order.get_created_at()
        self.assertIsInstance(created_at, datetime)


if __name__ == "__main__":
    unittest.main()
