## Exercise
Write a program to create a bank account manager where users can create accounts, deposit, withdraw, and check balance.

## Reference Solution
```python
class BankAccount:
    def __init__(self, account_number, account_name, balance=0):
        """
        Initialize a new bank account.

        :param account_number: Unique account number
        :param account_name: Account holder name
        :param balance: Initial balance (default: 0)
        """
        self.account_number = account_number
        self.account_name = account_name
        self.balance = balance

    def deposit(self, amount):
        """
        Deposit money into the account.

        :param amount: Amount to deposit
        :return: New balance
        """
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f} into account {self.account_number}. New balance: ${self.balance:.2f}")
            return self.balance
        else:
            print("Invalid deposit amount.")
            return None

    def withdraw(self, amount):
        """
        Withdraw money from the account.

        :param amount: Amount to withdraw
        :return: New balance
        """
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f} from account {self.account_number}. New balance: ${self.balance:.2f}")
            return self.balance
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            print("Insufficient funds.")
        return None

    def check_balance(self):
        """
        Check the current balance.

        :return: Current balance
        """
        print(f"Account {self.account_number} balance: ${self.balance:.2f}")
        return self.balance


class BankAccountManager:
    def __init__(self):
        """
        Initialize the bank account manager.
        """
        self.accounts = {}

    def create_account(self, account_number, account_name, balance=0):
        """
        Create a new bank account.

        :param account_number: Unique account number
        :param account_name: Account holder name
        :param balance: Initial balance (default: 0)
        """
        if account_number not in self.accounts:
            self.accounts[account_number] = BankAccount(account_number, account_name, balance)
            print(f"Account {account_number} created for {account_name}.")
        else:
            print("Account number already exists.")

    def get_account(self, account_number):
        """
        Get a bank account object.

        :param account_number: Unique account number
        :return: Bank account object or None if not found
        """
        return self.accounts.get(account_number)

    def list_accounts(self):
        """
        List all bank accounts.
        """
        print("Bank Accounts:")
        for account in self.accounts.values():
            print(f"Account Number: {account.account_number}, Account Name: {account.account_name}, Balance: ${account.balance:.2f}")


def main():
    manager = BankAccountManager()

    while True:
        print("\nBank Account Manager Menu:")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. List Accounts")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            account_number = input("Enter account number: ")
            account_name = input("Enter account name: ")
            balance = float(input("Enter initial balance (default: 0): ") or 0)
            manager.create_account(account_number, account_name, balance)
        elif choice == "2":
            account_number = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            account = manager.get_account(account_number)
            if account:
                account.deposit(amount)
            else:
                print("Account not found.")
        elif choice == "3":
            account_number = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            account = manager.get_account(account_number)
            if account:
                account.withdraw(amount)
            else:
                print("Account not found.")
        elif choice == "4":
            account_number = input("Enter account number: ")
            account = manager.get_account(account_number)
            if account:
                account.check_balance()
            else:
                print("Account not found.")
        elif choice == "5":
            manager.list_accounts()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
```

## Generated Output
```
Bank Account Manager Menu:
1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. List Accounts
6. Exit
Enter your choice: Invalid choice. Please try again.

Bank Account Manager Menu:
1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. List Accounts
6. Exit
Enter your choice: 
Traceback (most recent call last):
  File "/tmp/tmpgmu32yfg.py", line 146, in <module>
    main()
  File "/tmp/tmpgmu32yfg.py", line 107, in main
    choice = input("Enter your choice: ")
EOFError: EOF when reading a line
```

generated by python 3.10.13

solution generated by RedHatAI/Llama-3.3-70B-Instruct-FP8-dynamic
