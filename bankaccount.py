class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        # your code here
        self.balance += amount
        return self

    def withdraw(self, amount):
        # your code here
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance = self.balance - amount - 5
        return self

    def display_account_info(self):
        # your code here
        print(f"Balance : ${self.balance}")
        return self

    def yield_interest(self):
        # your code here
        if self.balance >= 0:
            self.balance = (self.balance * self.int_rate) + self.balance
        return self

user1 = BankAccount(0.01, 500)
user2 = BankAccount(0.02, 2000)

user1.deposit(100).deposit(50).deposit(350).withdraw(400).yield_interest().display_account_info()
user2.deposit(1000).deposit(450).withdraw(100).withdraw(350).withdraw(500).withdraw(20).yield_interest().display_account_info()