from app.models.library import Library
from app.models.order import Order
from app.interfaces.factory import Factory
from app.interfaces.observer import Librarian, OrderNotifier


def main():
    library = Library()
    notifier = OrderNotifier()
    librarian = Librarian()
    notifier.add_observer(librarian)

    users = {}
    orders = {}

    while True:
        print("\n=== Library Service ===")
        print("1. Додати книгу")
        print("2. Переглянути всі книги")
        print("3. Зареєструвати користувача")
        print("4. Зробити замовлення")
        print("5. Вийти")

        choice = input("Виберіть опцію: ")

        if choice == "1":
            title = input("Введіть назву книги: ")
            author = input("Введіть автора книги: ")
            year = int(input("Введіть рік видання: "))
            book = Factory.create_book(title, author, year)
            library.add_book(book)
            print("Книгу додано до бібліотеки.")

        elif choice == "2":
            books = library.get_all_books()
            if not books:
                print("Книг ще немає.")
            for b in books:
                print(f"- {b.get_title()} by {b.get_author()} ({b.get_year()})")

        elif choice == "3":
            name = input("Введіть імʼя: ")
            email = input("Введіть email: ")
            password = input("Введіть пароль: ")

            if email in users:
                print("Користувач з таким email вже існує.")
                continue

            user = Factory.create_user(name, email, password)
            users[email] = user
            print(f"Користувач зареєстрований з ID {user.get_id()}.")

        elif choice == "4":
            email = input("Введіть email користувача: ")
            user = users.get(email)

            if not user:
                print("Користувача не знайдено.")
                continue

            title = input("Введіть назву книги для замовлення: ")
            book = library.get_book(title)
            if not book:
                print("Книгу не знайдено.")
                continue

            order = Order(user, book)
            orders[order.get_id()] = order
            notifier.notify(
                f"Нове замовлення {order.get_id()} від користувача {user.get_name()} на книгу '{book.get_title()}'.")
            print(f"Замовлення створено з ID {order.get_id()}.")

        elif choice == "5":
            print("До побачення!")
            break
        else:
            print("Невірна опція. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
