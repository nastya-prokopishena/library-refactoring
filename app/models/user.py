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
        return self._user_id

    def get_name(self) -> str:
        return self._name

    def get_email(self) -> str:
        return self._email

    def verify_password(self, input_password: str) -> bool:
        return self._password_hash == self._hash_password(input_password)