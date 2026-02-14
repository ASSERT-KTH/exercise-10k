## Exercise
Create a function that helps the user track their personal expenses, allowing them to add and remove expenses and view their total spending.

## Reference Solution
```python
class ExpenseTracker:
    def __init__(self):
        """
        Initialize the expense tracker with an empty dictionary to store expenses.
        """
        self.expenses = {}

    def add_expense(self, category, amount, description=""):
        """
        Add a new expense to the tracker.

        Args:
        - category (str): The category of the expense (e.g., "Food", "Transportation", etc.).
        - amount (float): The amount of the expense.
        - description (str): An optional description of the expense.
        """
        if category in self.expenses:
            self.expenses[category].append({"amount": amount, "description": description})
        else:
            self.expenses[category] = [{"amount": amount, "description": description}]

    def remove_expense(self, category, index):
        """
        Remove an expense from the tracker.

        Args:
        - category (str): The category of the expense to remove.
        - index (int): The index of the expense to remove within the category.
        """
        if category in self.expenses and index < len(self.expenses[category]):
            del self.expenses[category][index]
        else:
            print("Invalid category or index.")

    def view_expenses(self, category=None):
        """
        View all expenses or expenses within a specific category.

        Args:
        - category (str): The category of expenses to view. If None, view all expenses.
        """
        if category:
            if category in self.expenses:
                print(f"Expenses in category '{category}':")
                for i, expense in enumerate(self.expenses[category]):
                    print(f"{i+1}. Amount: {expense['amount']}, Description: {expense['description']}")
            else:
                print("Category not found.")
        else:
            print("All expenses:")
            for category, expenses in self.expenses.items():
                print(f"Category: {category}")
                for i, expense in enumerate(expenses):
                    print(f"{i+1}. Amount: {expense['amount']}, Description: {expense['description']}")
                print()

    def total_spending(self, category=None):
        """
        Calculate the total spending or total spending within a specific category.

        Args:
        - category (str): The category of expenses to calculate the total spending for. If None, calculate the total spending for all categories.

        Returns:
        - float: The total spending.
        """
        total = 0
        if category:
            if category in self.expenses:
                for expense in self.expenses[category]:
                    total += expense["amount"]
            else:
                print("Category not found.")
        else:
            for expenses in self.expenses.values():
                for expense in expenses:
                    total += expense["amount"]
        return total


def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add expense")
        print("2. Remove expense")
        print("3. View expenses")
        print("4. View total spending")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            description = input("Enter description (optional): ")
            tracker.add_expense(category, amount, description)
        elif choice == "2":
            category = input("Enter category: ")
            index = int(input("Enter index of expense to remove: ")) - 1
            tracker.remove_expense(category, index)
        elif choice == "3":
            category = input("Enter category (or leave blank for all): ")
            if category:
                tracker.view_expenses(category)
            else:
                tracker.view_expenses()
        elif choice == "4":
            category = input("Enter category (or leave blank for all): ")
            if category:
                print(f"Total spending in category '{category}': {tracker.total_spending(category)}")
            else:
                print(f"Total spending: {tracker.total_spending()}")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
```

## Generated Output
```
Expense Tracker Menu:
1. Add expense
2. Remove expense
3. View expenses
4. View total spending
5. Exit
Enter your choice: Invalid choice. Please try again.

Expense Tracker Menu:
1. Add expense
2. Remove expense
3. View expenses
4. View total spending
5. Exit
Enter your choice: 
Traceback (most recent call last):
  File "/tmp/tmpn9tv81ha.py", line 122, in <module>
    main()
  File "/tmp/tmpn9tv81ha.py", line 92, in main
    choice = input("Enter your choice: ")
EOFError: EOF when reading a line
```

generated by python 3.10.13

solution generated by RedHatAI/Llama-3.3-70B-Instruct-FP8-dynamic
