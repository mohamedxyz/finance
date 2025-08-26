class BankAccount:
    def __init__(self, accountName: str, password: str, balance=0.0):
        self.accountName = accountName
        self._password = password
        self.balance = balance
        self._logged_in = False

    def login(self, name, password):
        if self.accountName == name and self._password == password:
            self._logged_in = True
            print("Login successful.")
        else:
            print("Login failed.")

    def logout(self):
        self._logged_in = False
        print("Logged out.")

    def _require_login(self):
        if not self._logged_in:
            print("Please login to perform this action.")
            return False
        return True

    def get_balance(self):
        if not self._require_login():
            return
        print(self.balance)

    def deposit(self, amount):
        if not self._require_login():
            return
        if amount > 0:
            self.balance += amount
            print("money deposited successfully")
            self.get_balance()
        else:
            print("you can't add negative amount of money! Try again.")

    def withdraw(self, amount):
        if not self._require_login():
            return
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print("money withdrawn successfully")
            self.get_balance()
        else:
            print("insufficient money, try again.")

    def transfer(self, other_account, amount):
        if not self._require_login():
            return
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount
            print(f"money transferd successfully to {other_account.accountName}.")
        else:
            print("Transfer failed: insufficient funds or invalid amount.")

