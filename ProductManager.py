import json
from Product import Product


class ProductManager:
    def __init__(self, filename):
        self.filename = filename
        self.products = self.load_products()

    def load_products(self):
        try:
            with open(self.filename, 'r') as file:
                products = json.load(file)
        except FileNotFoundError:
            products = []
        return [Product(**product) for product in products]

    def save_products(self):
        with open(self.filename, 'w') as file:
            products = [product.__dict__ for product in self.products]
            json.dump(products, file)

    def add_product(self, product):
        self.products.append(product)
        self.save_products()

    def edit_product(self, index, **kwargs):
        for key, value in kwargs.items():
            setattr(self.products[index], key, value)
        self.save_products()

    def delete_product(self, index):
        del self.products[index]
        self.save_products()

    def search_product(self, search_text):
        return [product for product in self.products if search_text.lower() in product.name.lower()]

    def display_products(self):
        print("{:<18} {:<18} {:<28} {:<18}"
              .format("Name", "Price", "Description", "Stock"))
        if not self.products:
            print("No products in products.")
        else:
            for i, product in enumerate(self.products):
                print("{:<18} {:<18} {:<28} {:<18}"
                      .format(product.name, product.price, product.description, product.stock))
        print("\n")
