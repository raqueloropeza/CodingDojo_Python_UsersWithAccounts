class BankAccount: 
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdrawal(self, amount):
        if (self.balance - amount) < 0:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= (amount +5)
        else:
            self.balance -= amount
        return self
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self


class User:
        def __init__(self, name, email_address):
            self.name = name
            self.email = email_address
            self.account = BankAccount(int_rate=0.02, balance=0)

        def make_deposit(self):	
            print(self.account.deposit())
            return self

        def make_withdrawal(self, amount):
            print(self.account.withdrawal(10))
            return self

        def display_user_balance(self):
            print(self.account.display_account_info())
            return self

        def transfer_money(self, other_user, amount):
            self.account_balance -= amount
            self = other_user
            self.account_balance += amount
            return self

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
rocky = User("Rocky Balboa", "rocky@python.com")

guido.account.deposit(100)
guido.account.deposit(200)
guido.account.withdrawal(50)
guido.account.display_account_info()



