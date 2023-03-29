class Product:
    def __init__(self, name, price, description, stock):
        self.name = name
        self.price = price
        self.description = description
        self.stock = stock

    def add_stock(self, amount):
        self.stock += amount

    def remove_stock(self, amount):
        self.stock -= amount

    def update_price(self, new_price):
        self.price = new_price

    def update_description(self, new_description):
        self.description = new_description

    def display_product(self):
        print(f"Product name: {self.name}")
        print(f"Product price: {self.price}")
        print(f"Product description: {self.description}")
        print(f"Product stock: {self.stock}")
