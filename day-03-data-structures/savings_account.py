from account import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=5):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def account_info(self):
        print("Account Type: Savings Account")
        print(f"Account Holder: {self.owner}")
        print(f"Interest Rate: {self.interest_rate}%")
        print(f"Account Balance: {self.balance}")

    