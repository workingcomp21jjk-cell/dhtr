class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number  # номер рахунку
        self.balance = balance  # баланс рахунку

    def deposit(self, amount):
        """Метод для поповнення рахунку"""
        if amount > 0:
            self.balance += amount
            print(f"Поповнено на {amount} грн. Новий баланс: {self.balance} грн.")
        else:
            print("Сума поповнення має бути більшою за 0!")

    def withdraw(self, amount):
        """Метод для зняття грошей"""
        if amount <= 0:
            print("Сума зняття має бути більшою за 0!")
        elif amount > self.balance:
            print("Недостатньо коштів на рахунку!")
        else:
            self.balance -= amount
            print(f"Знято {amount} грн. Залишок: {self.balance} грн.")

# приклад використання
account1 = BankAccount("UA123456789", 1000)

account1.deposit(500)     # поповнення
account1.withdraw(200)    # зняття
account1.withdraw(2000)   # спроба зняти більше, ніж є
