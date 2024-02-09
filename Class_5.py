class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, depos):
        self.balance += depos

    def withdraw(self, s):
        if s <= self.balance:
            self.balance -= s
        else:
            print(f"{self.owner}, negative balance")

    def __str__(self):
        return f"{self.owner} has {self.balance}$"