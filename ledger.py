from bank import BankAccount

ali = BankAccount("ali", 100)
ali.get_balance()
mohamed = BankAccount("mohamed", 100)
ali.transfer(mohamed, 100)
mohamed.get_balance()
