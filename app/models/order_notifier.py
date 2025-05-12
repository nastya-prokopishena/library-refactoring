class OrderNotifier:
    def notify(self, order: 'Order') -> None:
        print(f"Order {order.get_order_id()} has been created for user {order.get_user().get_name()}.")