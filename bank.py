class BankAccount:
    def __init__(self, owner, number, balance=0):
        self.owner = owner
        self.number = number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, owner, number, balance=0):
        self.accounts[number] = BankAccount(owner, number, balance)

    def deposit(self, number, amount):
        self.accounts[number].deposit(amount)

    def withdraw(self, number, amount):
        self.accounts[number].withdraw(amount)

    def transfer(self, from_num, to_num, amount):
        self.accounts[from_num].withdraw(amount)
        self.accounts[to_num].deposit(amount)
