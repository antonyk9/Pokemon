import random
class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def withdraw(self, amount):
        self.balance -= amount
    def deposit(self, amount):
        self.balance += amount
    def empty(self, balance):



        accounts = []
        for i in range(0, 10):
            name = "account" + str(i)
            balance = random.randint(1000, 2000)
            accounts.append(accounts(name, balance))

# deposit money
        for account in accounts:
            account.deposit(random.randint(500, 1000))
            print(account.balance)