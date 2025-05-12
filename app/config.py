from pymongo import MongoClient
import uuid


class MongoConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MongoConnection, cls).__new__(cls)
            cls._instance._client = MongoClient("mongodb://localhost:27017/")
            cls._instance._db = cls._instance._client["library_db"]
        return cls._instance

    @property
    def client(self):
        return self._client

    @property
    def db(self):
        return self._db


def generate_id() -> str:
    return str(uuid.uuid4())
