# 2. Class BankAccount with methods to deposit, withdraw, and check the balance

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        try:
            if amount > self.balance:
                raise ValueError("Insufficient funds")
            self.balance -= amount
        except ValueError as e:
            print(e)

    def get_balance(self):
        return self.balance
