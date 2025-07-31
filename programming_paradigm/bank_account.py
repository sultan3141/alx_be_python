class BankAccount:
    def __init__(self,account_balance):
        self.__account_balance =account_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        if amount <= self.__account_balance:
            self.__account_balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__account_balance
