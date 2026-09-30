from menuitem import MenuItem


class Menu:
    def __init__(self):
        # Stores menu items inside a dictionary
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