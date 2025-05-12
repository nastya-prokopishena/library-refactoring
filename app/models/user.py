from app.config import generate_id


class User:
    def __init__(self, name: str, email: str, password: str):
        self._id = generate_id()
        self._name = name
        self._email = email
        self._password = password

    def get_id(self) -> str:
        return self._id

    def get_name(self) -> str:
        return self._name

    def get_email(self) -> str:
        return self._email

    def get_password(self) -> str:
        return self._password
