## Exercise
Create a program that simulates the stock market using a while loop to handle user input and a for loop to iterate over the stocks.

## Reference Solution
```python
class Stock:
    def __init__(self, name, price):
        """
        Initialize a stock with a name and price.

        Args:
            name (str): The name of the stock.
            price (float): The current price of the stock.
        """
        self.name = name
        self.price = price

    def __str__(self):
        """
        Return a string representation of the stock.

        Returns:
            str: A string with the name and price of the stock.
        """
        return f"{self.name}: ${self.price:.2f}"

class StockMarket:
    def __init__(self):
        """
        Initialize a stock market with a list of stocks.
        """
        self.stocks = [
            Stock("Apple", 150.0),
            Stock("Google", 2500.0),
            Stock("Amazon", 3000.0),
            Stock("Microsoft", 200.0),
            Stock("Facebook", 250.0),
        ]
        self.portfolio = {}

    def display_stocks(self):
        """
        Display all the stocks in the market.
        """
        print("Available Stocks:")
        for i, stock in enumerate(self.stocks):
            print(f"{i + 1}. {stock}")

    def buy_stock(self):
        """
        Buy a stock.
        """
        self.display_stocks()
        stock_index = int(input("Enter the number of the stock you want to buy: ")) - 1
        if stock_index < 0 or stock_index >= len(self.stocks):
            print("Invalid stock number.")
            return

        stock = self.stocks[stock_index]
        quantity = int(input("Enter the quantity you want to buy: "))
        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return

        if stock.name in self.portfolio:
            self.portfolio[stock.name]["quantity"] += quantity
        else:
            self.portfolio[stock.name] = {"stock": stock, "quantity": quantity}

        print(f"You bought {quantity} shares of {stock.name}.")

    def sell_stock(self):
        """
        Sell a stock.
        """
        if not self.portfolio:
            print("You don't have any stocks to sell.")
            return

        print("Your Portfolio:")
        for i, (stock_name, stock_info) in enumerate(self.portfolio.items()):
            print(f"{i + 1}. {stock_info['stock']} - Quantity: {stock_info['quantity']}")

        stock_index = int(input("Enter the number of the stock you want to sell: ")) - 1
        if stock_index < 0 or stock_index >= len(self.portfolio):
            print("Invalid stock number.")
            return

        stock_name = list(self.portfolio.keys())[stock_index]
        stock_info = self.portfolio[stock_name]
        quantity = int(input("Enter the quantity you want to sell: "))
        if quantity <= 0 or quantity > stock_info["quantity"]:
            print("Quantity must be greater than zero and not exceed the quantity you own.")
            return

        if quantity == stock_info["quantity"]:
            del self.portfolio[stock_name]
        else:
            self.portfolio[stock_name]["quantity"] -= quantity

        print(f"You sold {quantity} shares of {stock_name}.")

    def display_portfolio(self):
        """
        Display the user's portfolio.
        """
        if not self.portfolio:
            print("You don't have any stocks in your portfolio.")
            return

        print("Your Portfolio:")
        total_value = 0
        for stock_name, stock_info in self.portfolio.items():
            print(f"{stock_info['stock']} - Quantity: {stock_info['quantity']}")
            total_value += stock_info["stock"].price * stock_info["quantity"]

        print(f"Total Value: ${total_value:.2f}")

def main():
    market = StockMarket()
    while True:
        print("\nStock Market Simulator")
        print("1. Display Stocks")
        print("2. Buy Stock")
        print("3. Sell Stock")
        print("4. Display Portfolio")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            market.display_stocks()
        elif choice == "2":
            market.buy_stock()
        elif choice == "3":
            market.sell_stock()
        elif choice == "4":
            market.display_portfolio()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```

## Generated Output
```
Stock Market Simulator
1. Display Stocks
2. Buy Stock
3. Sell Stock
4. Display Portfolio
5. Exit
Enter your choice: Invalid choice. Please try again.

Stock Market Simulator
1. Display Stocks
2. Buy Stock
3. Sell Stock
4. Display Portfolio
5. Exit
Enter your choice: 
Traceback (most recent call last):
  File "/tmp/tmp6slptb99.py", line 139, in <module>
    main()
  File "/tmp/tmp6slptb99.py", line 123, in main
    choice = input("Enter your choice: ")
EOFError: EOF when reading a line
```

generated by python 3.10.13

solution generated by RedHatAI/Llama-3.3-70B-Instruct-FP8-dynamic
