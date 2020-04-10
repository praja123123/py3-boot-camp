class BankAccount:
    """
    This class defines Bank Account
    Attributes: owner, balance
    """
    def __init__(self, owner, balance=0):
        """Create object of Bank Account class"""
        self.owner = owner
        self.balance = balance

    def __str__(self):

        return f'Account owner:   {self.owner} \n' \
               f'Account balance: ${self.balance}'

    def deposit(self, value):

        self.balance += value
        print('Deposit Accepted.')

    def withdraw(self, value):

        if self.balance - value >= 0:
            self.balance -= value
            print('Withdraw Accepted.')
        else:
            print('Funds Unavailable!')

acct1 = BankAccount('Marcin', 100)
acct1.deposit(50)
acct1.withdraw(75)
acct1.withdraw(500)
acct1.withdraw(75)
print(acct1)

print(BankAccount.__doc__)