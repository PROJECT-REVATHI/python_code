class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item_name, qty):
        self.items.append((item_name, qty))

    def remove_item(self, item_name):
        self.items = [item for item in self.items if item[0] != item_name]

    def calculate_total(self):
        return sum(item[1] for item in self.items)

# Example usage
cart = ShoppingCart()
cart.add_item("Papaya", 100)
cart.add_item("Guava", 200)
cart.add_item("Orange", 150)

print("Current Items in Cart:")
for item in cart.items:
    print(f"{item[0]} - {item[1]}")

print("Total Quantity:", cart.calculate_total())

cart.remove_item("Orange")
print("\nUpdated Items in Cart after removing Orange:")
for item in cart.items:
    print(f"{item[0]} - {item[1]}")

print("Total Quantity:", cart.calculate_total())
