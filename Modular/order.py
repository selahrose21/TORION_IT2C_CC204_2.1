from orderitem import OrderItem


class Order:
    def __init__(self):
        self.order_items = []

    def add_item(self, menu_item, quantity):
        order_item = OrderItem(menu_item, quantity)
        self.order_items.append(order_item)
        return order_item.calculate_line_total()

    def calculate_subtotal(self):
        subtotal = 0.0
        for item in self.order_items:
            subtotal += item.calculate_line_total()
        return subtotal

    def calculate_discount(self, subtotal):
        if subtotal >= 500.0:
            return subtotal * 0.10
        return 0.0

    def print_receipt(self):
        subtotal = self.calculate_subtotal()
        discount = self.calculate_discount(subtotal)
        total_due = subtotal - discount

        print("\n==================================================")
        print("                 FRIDAY'S RESTAURANT              ")
        print("              Official Sales Receipt              ")
        print("==================================================")
        print(f"{'Item':<24} {'Qty':<5} {'Price':<8} {'Total':>10}")
        print("--------------------------------------------------")

        for item in self.order_items:
            line_total = item.calculate_line_total()
            print(
                f"{item.menu_item.name:<24} {item.quantity:<5} {item.menu_item.price:<8.2f} {line_total:>10.2f}"
            )

        print("--------------------------------------------------")
        print(f"{'Subtotal:':<38} PHP {subtotal:>8.2f}")

        if discount > 0:
            print(f"{'Discount (10% off >= PHP 500):':<38}-PHP {discount:>8.2f}")

        print("==================================================")
        print(f"{'TOTAL AMOUNT DUE:':<38} PHP {total_due:>8.2f}")
        print("==================================================")
        print("         Thank you for dining with us!            ")
        print("==================================================\n")