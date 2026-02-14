## Exercise
Write a program that simulates a simple e-commerce website, allowing the user to add, remove, and view products

## Reference Solution
```python
# ecommerce_website.py

class Product:
    def __init__(self, name, price, quantity):
        """
        Initialize a Product object.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The quantity of the product.
        """
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        """
        Return a string representation of the Product object.
        """
        return f"{self.name}: ${self.price:.2f} ({self.quantity} in stock)"


class ShoppingCart:
    def __init__(self):
        """
        Initialize a ShoppingCart object.
        """
        self.products = {}

    def add_product(self, product, quantity):
        """
        Add a product to the shopping cart.

        Args:
            product (Product): The product to add.
            quantity (int): The quantity of the product to add.
        """
        if product.name in self.products:
            self.products[product.name]["quantity"] += quantity
        else:
            self.products[product.name] = {"product": product, "quantity": quantity}

    def remove_product(self, product_name, quantity):
        """
        Remove a product from the shopping cart.

        Args:
            product_name (str): The name of the product to remove.
            quantity (int): The quantity of the product to remove.
        """
        if product_name in self.products:
            if self.products[product_name]["quantity"] <= quantity:
                del self.products[product_name]
            else:
                self.products[product_name]["quantity"] -= quantity
        else:
            print(f"Product '{product_name}' not found in cart.")

    def view_cart(self):
        """
        Print the contents of the shopping cart.
        """
        print("Shopping Cart:")
        for product_name, product_info in self.products.items():
            print(f"{product_info['product']} x {product_info['quantity']}")


class ECommerceWebsite:
    def __init__(self):
        """
        Initialize an ECommerceWebsite object.
        """
        self.products = []
        self.shopping_cart = ShoppingCart()

    def add_product(self):
        """
        Add a product to the website.
        """
        name = input("Enter product name: ")
        price = float(input("Enter product price: $"))
        quantity = int(input("Enter product quantity: "))
        product = Product(name, price, quantity)
        self.products.append(product)
        print(f"Product '{name}' added successfully.")

    def remove_product(self):
        """
        Remove a product from the website.
        """
        name = input("Enter product name: ")
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                print(f"Product '{name}' removed successfully.")
                return
        print(f"Product '{name}' not found.")

    def view_products(self):
        """
        Print the products available on the website.
        """
        print("Available Products:")
        for product in self.products:
            print(product)

    def start(self):
        """
        Start the e-commerce website simulator.
        """
        while True:
            print("\nE-Commerce Website Simulator")
            print("1. Add Product")
            print("2. Remove Product")
            print("3. View Products")
            print("4. Add to Cart")
            print("5. Remove from Cart")
            print("6. View Cart")
            print("7. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_product()
            elif choice == "2":
                self.remove_product()
            elif choice == "3":
                self.view_products()
            elif choice == "4":
                self.view_products()
                name = input("Enter product name to add to cart: ")
                quantity = int(input("Enter quantity to add to cart: "))
                for product in self.products:
                    if product.name == name:
                        self.shopping_cart.add_product(product, quantity)
                        print(f"Product '{name}' added to cart successfully.")
                        break
                else:
                    print(f"Product '{name}' not found.")
            elif choice == "5":
                self.shopping_cart.view_cart()
                name = input("Enter product name to remove from cart: ")
                quantity = int(input("Enter quantity to remove from cart: "))
                self.shopping_cart.remove_product(name, quantity)
            elif choice == "6":
                self.shopping_cart.view_cart()
            elif choice == "7":
                print("Exiting simulator. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    website = ECommerceWebsite()
    website.start()
```

## Generated Output
```
E-Commerce Website Simulator
1. Add Product
2. Remove Product
3. View Products
4. Add to Cart
5. Remove from Cart
6. View Cart
7. Exit
Enter your choice: Invalid choice. Please try again.

E-Commerce Website Simulator
1. Add Product
2. Remove Product
3. View Products
4. Add to Cart
5. Remove from Cart
6. View Cart
7. Exit
Enter your choice: 
Traceback (most recent call last):
  File "/tmp/tmpba6v5aib.py", line 155, in <module>
    website.start()
  File "/tmp/tmpba6v5aib.py", line 121, in start
    choice = input("Enter your choice: ")
EOFError: EOF when reading a line
```

generated by python 3.10.13

solution generated by RedHatAI/Llama-3.3-70B-Instruct-FP8-dynamic
