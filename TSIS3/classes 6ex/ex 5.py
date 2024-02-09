class Account():
    def __init__(some, owner, balance = 0):
        some.owner = owner
        some.balance = balance
    def deposit(some, money):
        some.balance += money
        print(f"Deposit of {money} successful. New balance: {some.balance}")
    def withdraw(some, money):
        if some.balance - money >= 0:
            some.balance -= money
            print(f"Withdrawal of {money} successful. New balance: {some.balance}")
        else:
            print(f"Withdrawal of {money} failed due to insufficient funds.")