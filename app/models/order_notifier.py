class OrderNotifier:
    def notify(self, order: 'Order') -> None:
        print(f"New order created: Order ID {order.get_order_id()}, "
              f"User: {order.get_user().get_name()}, "
              f"Book: {order.get_book().get_title()}")