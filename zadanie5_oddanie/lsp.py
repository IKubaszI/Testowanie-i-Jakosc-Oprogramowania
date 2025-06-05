from abc import ABC, abstractmethod

class InsufficientFundsException(Exception):
    pass

class MinimumBalanceException(Exception):
    pass

class BankAccount(ABC):
    def __init__(self):
        self._balance = 0

    def deposit(self, amount):
        self._balance += amount

    @abstractmethod
    def withdraw(self, amount):
        pass

    def get_balance(self):
        return self._balance

class RegularAccount(BankAccount):
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            raise InsufficientFundsException("Insufficient funds")

class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        minimum_balance = 100
        if self._balance - amount >= minimum_balance:
            self._balance -= amount
        else:
            raise MinimumBalanceException("Minimum balance for savings account is 100")

def perform_transaction(account: BankAccount, deposit_amount, withdraw_amount):
    account.deposit(deposit_amount)
    try:
        account.withdraw(withdraw_amount)
        print(f"Balance after transaction: {account.get_balance()}")
    except Exception as e:
        print(f"Transaction failed: {e}")

regular_account = RegularAccount()
savings_account = SavingsAccount()
perform_transaction(regular_account, 500, 200)
perform_transaction(savings_account, 500, 450)
