class InvalidPinException(Exception):
    pass

class InsufficientFundsException(Exception):
    pass

class ATM:
    def __init__(self, pin: int, balance: float = 0.00):
        self.pin = pin
        self.balance = balance

    def check_balance(self, pin: int) -> float:
        if pin != self.pin:
            raise InvalidPinException("Nieprawidłowy PIN.")
        return self.balance

    def deposit(self, pin: int, amount: float) -> float:
        if pin != self.pin:
            raise InvalidPinException("Nieprawidłowy PIN.")
        if amount < 0:
            raise ValueError("Kwota wpłaty musi być dodatnia i większa od zera.")
        self.balance += amount
        return self.balance

    def withdraw(self, pin: int, amount: float) -> float:
        if pin != self.pin:
            raise InvalidPinException("Nieprawidłowy PIN.")
        if amount < 0:
            raise ValueError("Wypłacana kwota musi być dodatnia i większa od zera.")
        if amount > self.balance:
            raise InsufficientFundsException("Niewystarczające środki na koncie.")
        self.balance -= amount
        return self.balance
