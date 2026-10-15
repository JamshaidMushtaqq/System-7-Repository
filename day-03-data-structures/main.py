from savings_account import SavingsAccount

def main():
    account1 = SavingsAccount("Jamshaid", 1000, 3)
    account2 = SavingsAccount("Faizan", 500, 4)

    print("\n---------jamshaid's Account Info---------")
    account1.account_info()
    account1.deposit(200)
    account1.withdraw(100)
    account1.show_balance()

    print("\n---------Faizan's Account Info---------")
    account2.account_info()
    account2.show_balance()

    print("\n---------Polymorphisam Demo---------")

    accounts = [account1, account2]

    for account in accounts:
        account.account_info()


if __name__ == "__main__":
    main()
