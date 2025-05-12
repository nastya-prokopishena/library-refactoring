class User:
    def __init__(self, user_id: str, name: str):
        self._user_id = user_id
        self._name = name

    def get_user_id(self) -> str:
        return self._user_id

    def get_name(self) -> str:
        return self._name
