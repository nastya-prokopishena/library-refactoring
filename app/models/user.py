from typing import Optional
import hashlib


class User:
    def __init__(self, user_id: str, name: str, email: str, password: str):
        self._user_id = user_id
        self._name = name
        self._email = email
        self._password_hash = self._hash_password(password)

    def _hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    def get_user_id(self) -> str:
        pass

    def get_name(self) -> str:
        pass

    def get_email(self) -> str:
        pass

    def verify_password(self, input_password: str) -> bool:
        pass