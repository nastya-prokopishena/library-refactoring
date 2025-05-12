from datetime import datetime


class Order:
    def __init__(self, order_id: str, user: 'User', book: 'Book'):
        self._order_id = order_id
        self._user = user
        self._book = book
        self._created_at = datetime.now()

    def get_order_id(self) -> str:
        pass

    def get_user(self) -> 'User':
        pass

    def get_book(self) -> 'Book':
        pass

    def get_created_at(self) -> datetime:
        pass