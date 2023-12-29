class Bank_account():
    def __init__(self, account_number):
        self.num=account_number
        self.amount=0

    def deposit(self, sum):
        self.amount+=sum
    def withdraw(self, sum):
        if sum<=self.amount:
            self.amount-=sum
        else:
            print("Insufficient funds on the account")
    def show(self):
        print(f"Bank account: {self.num}")
        print(f"Balance: PLN {self.amount}")


account=Bank_account("12 3456 5555 9090 1111 0000 7722")

account.show()
account.deposit(25.30)
account.show()
account.withdraw(31.70)
account.show()
account.withdraw(14)
account.show()