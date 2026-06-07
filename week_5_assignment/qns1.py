# qns 1
class BankAccount:

    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"NPR {amount} deposited into {self.account_number}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"NPR {amount} withdrawn from {self.account_number}")

    def get_balance(self):
        print(f"{self.name} ({self.account_number}) - Balance: NPR {self.balance}")

accounts = [
    ("Ramesh Thapa", "A001", 5000),
    ("Sunita Karki", "A002", 0),
    ("Bikash Rai", "A003", 12000)
]

bank_accounts = []

for name, acc_no, balance in accounts:
    bank_accounts.append(BankAccount(name, acc_no, balance))

bank_accounts[1].deposit(3000)
bank_accounts[2].withdraw(15000)
bank_accounts[0].withdraw(2000)

print("\nFinal Balances:")
for account in bank_accounts:
    account.get_balance()
