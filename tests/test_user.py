import unittest
from app.models import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("Anastasiia", "prokopishena.anastasia@gmail.com", "password123")

    def test_get_id(self):
        self.assertIsInstance(self.user.get_id(), str)

    def test_get_name(self):
        self.assertEqual(self.user.get_name(), "Anastasiia")

    def test_get_email(self):
        self.assertEqual(self.user.get_email(), "prokopishena.anastasia@gmail.com")

    def test_get_password(self):
        self.assertEqual(self.user.get_password(), "password123")


if __name__ == "__main__":
    unittest.main()
