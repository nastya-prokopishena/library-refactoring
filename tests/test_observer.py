from app.interfaces.observer import OrderNotifier, Librarian


def test_observer_notified():
    notifier = OrderNotifier()
    librarian = Librarian()

    # Перехопимо повідомлення
    messages = []

    def custom_update(message):
        messages.append(message)

    # Замінимо метод update на наш
    librarian.update = custom_update

    notifier.add_observer(librarian)
    notifier.notify("Тестове замовлення")

    assert len(messages) == 1
    assert messages[0] == "Тестове замовлення"


def test_observer_multiple_notifiers():
    notifier = OrderNotifier()
    librarian1 = Librarian()
    librarian2 = Librarian()

    # Перехоплення повідомлень
    messages = []

    librarian1.update = lambda msg: messages.append(f"L1: {msg}")
    librarian2.update = lambda msg: messages.append(f"L2: {msg}")

    notifier.add_observer(librarian1)
    notifier.add_observer(librarian2)

    notifier.notify("Замовлення №1")
    assert len(messages) == 2
    assert "L1: Замовлення №1" in messages
    assert "L2: Замовлення №1" in messages


def test_observer_prevents_duplicate_observers():
    notifier = OrderNotifier()
    librarian = Librarian()

    messages = []
    librarian.update = lambda msg: messages.append(msg)

    notifier.add_observer(librarian)
    notifier.add_observer(librarian)

    notifier.notify("Нове замовлення")

    assert len(messages) == 1
    assert messages[0] == "Нове замовлення"
