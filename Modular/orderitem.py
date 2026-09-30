class OrderItem:
    def __init__(self, menu_item, quantity):
        self.menu_item = menu_item
        self.quantity = quantity

    # Calculate total for this item
    def calculate_line_total(self):
        return self.menu_item.price * self.quantity