class Observer:
    def update(self, message: str) -> None:
        pass


class Librarian(Observer):
    def update(self, message: str) -> None:
        print(f"Librarian Notification: {message}")


class OrderNotifier:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def notify(self, message: str) -> None:
        for observer in self._observers:
            observer.update(message)
