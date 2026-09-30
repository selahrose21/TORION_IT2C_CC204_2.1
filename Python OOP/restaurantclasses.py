class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Menu:
    def __init__(self):
        self.items = {
            1: MenuItem("Friday Fine Burger", 145.00),
            2: MenuItem("Friday Flaky Fries", 87.00),
            3: MenuItem("Friday Fresh Soup", 97.00),
            4: MenuItem("Friday Fluffy Pancakes", 87.00),
            5: MenuItem("Friday Friends' Slushies", 95.00),
            6: MenuItem("Friday Frothy Coffees", 120.00),
            7: MenuItem("Friday Fudgy Pastries", 75.00),
        }

    def display_menu(self):
        print("\n==================================================")
        print("            WELCOME TO FRIDAY'S FOOD              ")
        print("==================================================")
        print(f"{'No.':<4} {'Item Name':<28} {'Price (PHP)':>15}")
        print("--------------------------------------------------")

        for item_num, item in self.items.items():
            print(f"{item_num:<4} {item.name:<28} {item.price:>15.2f}")

        print("--------------------------------------------------")

    def get_item(self, choice):
        return self.items.get(choice)


class OrderItem:
    def __init__(self, menu_item, quantity):
        self.menu_item = menu_item
        self.quantity = quantity

    def calculate_line_total(self):
        return self.menu_item.price * self.quantity


class Order:
    def __init__(self):
        # List to store OrderItem objects
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


class RestaurantSystem:
    def __init__(self):
        self.menu = Menu()
        self.order = Order()

    def start(self):
        # Show menu
        self.menu.display_menu()

        start_choice = (
            input("\nDo you want to place an order? (yes/no): ").strip().lower()
        )

        if start_choice not in ["yes", "y"]:
            print("\nThank you for visiting Friday's! Have a great day!")
            return

        ordering = True
        while ordering:
            try:
                choice = int(input("\nEnter item number (1-7): "))
                selected_item = self.menu.get_item(choice)

                if selected_item:
                    quantity = int(
                        input(f"Enter quantity for {selected_item.name}: ")
                    )

                    if quantity > 0:
                        line_total = self.order.add_item(
                            selected_item, quantity
                        )
                        print(
                            f"--> Added {quantity}x {selected_item.name} (PHP {line_total:.2f})"
                        )
                    else:
                        print("Quantity must be at least 1.")
                        continue
                else:
                    print("Invalid item number. Choose between 1 and 7.")
                    continue

            except ValueError:
                print("Please enter numbers only.")
                continue

            while True:
                again = (
                    input("\nDo you want to order another item? (yes/no): ")
                    .strip()
                    .lower()
                )
                if again in ["yes", "y"]:
                    break
                elif again in ["no", "n"]:
                    ordering = False
                    break
                else:
                    print("Please enter 'yes' or 'no'.")

        if self.order.order_items:
            self.order.print_receipt()