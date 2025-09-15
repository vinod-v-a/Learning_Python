"Inventory Management System"

class Item:
    def __init__(self, name, category, price, quantity):
        self.name = name
        self.category = category
        self.__price = price          # private
        self.__quantity = quantity    # private

    def update_quantity(self, amount):
        if self.__quantity + amount >= 0:
            self.__quantity += amount
        else:
            print("Quantity cannot be negative")

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Category: {self.category}")
        print(f"Price: ${self.__price}")
        print(f"Quantity: {self.__quantity}")

class Electronics(Item):
    def __init__(self, name, category, price, quantity, warranty_period):
        super().__init__(name, category, price, quantity)
        self.warranty_period = warranty_period

    def display_info(self):
        super().display_info()
        print(f"Warranty Period: {self.warranty_period}")

class Furniture(Item):
    def __init__(self, name, category, price, quantity, material, dimensions):
        super().__init__(name, category, price, quantity)
        self.material = material
        self.dimensions = dimensions
    def display_info(self):
        super().display_info()
        print(f"Material: {self.material}")
        print(f"Dimensions: {self.dimensions}")



# Example Usage
elec = Electronics("Smartphone", "Electronics", 999, 10, "2 years")
furn = Furniture("Dining Table", "Furniture", 500, 5, "Wood", "6ft x 3ft x 3ft")

print("=== Electronics Info ===")
elec.display_info()


print("\n=== Furniture Info ===")
furn.display_info()



