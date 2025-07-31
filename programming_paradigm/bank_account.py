class BankAccount:
    def __init__(self, account_balance):
        self.__account_balance = account_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited: ${amount:.1f}")  # 1 decimal place

    def withdraw(self, amount):
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrew: ${amount:.1f}")  # 1 decimal place
        else:
            print("Insufficient funds.")  # Single print

    def get_balance(self):
        return self.__account_balance

    def display_balance(self):
        print(f"Current Balance: ${self.__account_balance:.1f}")  # Match expected format

