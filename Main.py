from ProductManager import ProductManager
from Product import Product

manager = ProductManager("products.json")

while True:
    print("\n              PRODUCT MANAGER PROGRAM")
    print("*************************MENU**************************")
    print("**  1. Add Product.                                  **")
    print("**  2. Edit Product By ID.                           **")
    print("**  3. Delete Product.                               **")
    print("**  4. Search Product By Name.                       **")
    print("**  5. Display Products.                             **")
    print("**  6. Exit.                                         **")
    print("*******************************************************")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Insert name : ")
        price = input("Insert price : ")
        description = input("Insert description: ")
        stock = input("Insert stock: ")
        product = Product(name, price, description, stock)
        manager.add_product(product)
        print("Product added.")
    elif choice == "2":
        index = int(input("Enter product index: ")) - 1
        product = manager.products[index]
        print(f"Editing product: {product.name}")
        name = input(f"Enter new name ({product.name}): ") or price.name
        price = input(f"Enter new price ({product.price}): ") or price.price
        description = input(
            f"Enter new description ({product.description}): ") or product.description
        stock = input(f"Enter new stock ({product.stock}): ") or product.stock
        manager.edit_product(index,
                             name=name, price=price, description=description, stock=stock)
        print("Product edited.")
    elif choice == "3":
        index = int(input("Enter product index: ")) - 1
        product = manager.products[index]
        print(f"Deleting product: {product.name}")
        confirm = input("Are you sure? (y/n): ")
        if confirm.lower() == "y":
            manager.delete_product(index)
            print("Product deleted.")
    elif choice == "4":
        search_text = input("Enter search text: ")
        results = manager.search_product(search_text)
        if results:
            print("Search results:")
            for i, product in enumerate(results):
                print(
                    f"{i + 1} {product.name} {product.price} {product.description} {product.stock}")
        else:
            print("No results.")
    elif choice == "5":
        manager.display_products()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again.")
