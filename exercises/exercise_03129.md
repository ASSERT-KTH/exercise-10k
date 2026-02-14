## Exercise
Create a program that allows the user to create, deposit, and withdraw from a bank account.

## Reference Solution
```python
class BankAccount:
    def __init__(self, account_number, account_name, balance=0.0):
        """
        Initialize a bank account.

        Args:
            account_number (str): The account number.
            account_name (str): The account holder's name.
            balance (float, optional): The initial balance. Defaults to 0.0.
        """
        self.account_number = account_number
        self.account_name = account_name
        self.balance = balance

    def deposit(self, amount):
        """
        Deposit money into the account.

        Args:
            amount (float): The amount to deposit.
        """
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f} into account {self.account_number}. New balance: ${self.balance:.2f}")
        else:
            print("Invalid deposit amount. Please enter a positive number.")

    def withdraw(self, amount):
        """
        Withdraw money from the account.

        Args:
            amount (float): The amount to withdraw.
        """
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f} from account {self.account_number}. New balance: ${self.balance:.2f}")
        elif amount <= 0:
            print("Invalid withdrawal amount. Please enter a positive number.")
        else:
            print("Insufficient funds.")

    def display_account_info(self):
        """
        Display the account information.
        """
        print(f"Account Number: {self.account_number}")
        print(f"Account Name: {self.account_name}")
        print(f"Balance: ${self.balance:.2f}")


class Bank:
    def __init__(self):
        """
        Initialize the bank.
        """
        self.accounts = {}

    def create_account(self, account_number, account_name, balance=0.0):
        """
        Create a new bank account.

        Args:
            account_number (str): The account number.
            account_name (str): The account holder's name.
            balance (float, optional): The initial balance. Defaults to 0.0.
        """
        if account_number not in self.accounts:
            self.accounts[account_number] = BankAccount(account_number, account_name, balance)
            print(f"Account {account_number} created successfully.")
        else:
            print("Account number already exists.")

    def get_account(self, account_number):
        """
        Get a bank account by account number.

        Args:
            account_number (str): The account number.

        Returns:
            BankAccount: The bank account object.
        """
        return self.accounts.get(account_number)

    def display_account_info(self, account_number):
        """
        Display the account information.

        Args:
            account_number (str): The account number.
        """
        account = self.get_account(account_number)
        if account:
            account.display_account_info()
        else:
            print("Account not found.")


def main():
    bank = Bank()

    while True:
        print("\n1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Display Account Info")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            account_number = input("Enter account number: ")
            account_name = input("Enter account holder's name: ")
            balance = float(input("Enter initial balance (default=0.0): ") or 0.0)
            bank.create_account(account_number, account_name, balance)
        elif choice == "2":
            account_number = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            account = bank.get_account(account_number)
            if account:
                account.deposit(amount)
            else:
                print("Account not found.")
        elif choice == "3":
            account_number = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            account = bank.get_account(account_number)
            if account:
                account.withdraw(amount)
            else:
                print("Account not found.")
        elif choice == "4":
            account_number = input("Enter account number: ")
            bank.display_account_info(account_number)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
```

## Generated Output
```
1. Create Account
2. Deposit
3. Withdraw
4. Display Account Info
5. Exit
Enter your choice: Invalid choice. Please try again.

1. Create Account
2. Deposit
3. Withdraw
4. Display Account Info
5. Exit
Enter your choice: 
Traceback (most recent call last):
  File "/tmp/tmp6q8gygy9.py", line 143, in <module>
    main()
  File "/tmp/tmp6q8gygy9.py", line 110, in main
    choice = input("Enter your choice: ")
EOFError: EOF when reading a line
```

generated by python 3.10.13

solution generated by RedHatAI/Llama-3.3-70B-Instruct-FP8-dynamic
