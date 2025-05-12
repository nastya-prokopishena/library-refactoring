import unittest
from app.models import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("1", "Anastasiia", "prokopishena.anastasia@gmail.com", "password123")

    def test_get_user_id(self):
        self.assertEqual(self.user.get_user_id(), "1")

    def test_get_name(self):
        self.assertEqual(self.user.get_name(), "Anastasiia")

    def test_get_email(self):
        self.assertEqual(self.user.get_email(), "prokopishena.anastasia@gmail.com")

    def test_verify_password_correct(self):
        self.assertTrue(self.user.verify_password("password123"))



if __name__ == "__main__":
    unittest.main()
