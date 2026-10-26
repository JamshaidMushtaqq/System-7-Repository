from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self,owner,balance):
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print("Deposit successfuly")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            print("Withdrawal successfuly")
        else:
            print("Insufficient funds or invalid amount")

    def show_balance(self):
        print(f"Account owner: {self.owner}")
        print(f"Account balance: {self._balance}")

    @abstractmethod
    def account_info(self):
        pass
    