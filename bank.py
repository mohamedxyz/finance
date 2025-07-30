# TODO: add a login so that transactions must have been verified by an account
class BankAccount:
    def __init__(self, accountName: str, balance=0.0):
        self.accountName = accountName
        self.balance = balance

    def get_balance(self):
        print(self.balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("money deposited successfully")
            self.get_balance()
        else:
            print("you can't add negative amount of money! Try again.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print("money withdrawn successfully")
            self.get_balance()
        else:
            print("insufficient money, try again.")

    def transfer(self, other_account, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.other_account = other_account
            other_account.balance += amount
            print(
                f"money transferd successfully to {other_account.accountName}.")
        else:
            print("Transfer failed: insufficient funds or invalid amount.")
