from app.interfaces.factory import Factory
from app.models.user import User
from app.models.book import Book


def test_factory_create_user():
    user = Factory.create_user("Іван", "ivan@example.com", "password123")
    assert isinstance(user, User)
    assert user.get_name() == "Іван"
    assert user.get_email() == "ivan@example.com"
    assert user.get_password() == "password123"
    assert len(user.get_id()) > 0  # Перевірка, що ID згенеровано


def test_factory_create_book():
    book = Factory.create_book("Місто", "Валер'ян Підмогильний", 1927)
    assert isinstance(book, Book)
    assert book.get_title() == "Місто"
    assert book.get_author() == "Валер'ян Підмогильний"
    assert book.get_year() == 1927


def test_user_has_unique_id():
    user1 = Factory.create_user("User1", "u1@example.com", "pass1")
    user2 = Factory.create_user("User2", "u2@example.com", "pass2")
    assert user1.get_id() != user2.get_id()


def test_book_attributes():
    book = Factory.create_book("Захар Беркут", "Іван Франко", 1883)
    assert book.get_title() == "Захар Беркут"
    assert book.get_author() == "Іван Франко"
    assert book.get_year() == 1883
