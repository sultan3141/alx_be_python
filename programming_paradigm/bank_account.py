class BankAccount:
    def __init__(self, account_balance):
        self.__account_balance = account_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f'Deposited: ${amount}')  # (optional if your test expects this)

    def withdraw(self, amount):
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f'Withdrew: ${amount}')  
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__account_balance

    def display_balance(self):
        print(f"Current Balance: {self.__account_balance}")

