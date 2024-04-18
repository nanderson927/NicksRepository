from bank_account import BankAccount #imports class

#creates objects
account1 = BankAccount(123456, 50.00)
account2 = BankAccount(333222)

#calls __str__
print(account1)
print(account2)

#uses methods
account1.withdraw(15.00)
account2.deposit(30.00)

print(account1)
print(account2)

#uses get_balance
print(account1.get_balance())




