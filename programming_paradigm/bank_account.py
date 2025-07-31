class BankAccount:
    def __init__(self, account_balance):
        self.__account_balance = account_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited: ${amount:.1f}")  # match test format

    def withdraw(self, amount):
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"Withdrew: ${amount:.1f}")
            return True
        else:
            print("Insufficient funds.")
            return False

    def get_balance(self):
        return self.__account_balance

    def display_balance(self):
        print(f"Current Balance: ${self.__account_balance:.2f}")  # match test format


