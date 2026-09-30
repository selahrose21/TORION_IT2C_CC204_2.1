from menu import Menu
from order import Order


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


if __name__ == "__main__":
    system = RestaurantSystem()
    system.start()