class InvalidPinException(Exception):
    pass
class InsufficientFundsException(Exception):
    pass
class ATM:
    """
    Klasa reprezentujÄca bankomat (ATM) z podstawowymi operacjami bankowymi.
    """
    def __init__(self,pin: int, balance: float = 0.00):
        self.pin = pin
        self.balance = balance

    def check_balance(self, pin: int) -> float:

        if pin != self.pin:
            raise InvalidPinException("Nieprawidłowy PIN.")
        return self.balance


    def deposit(self, pin: int, amount: float) -> float:

        if pin != self.pin:
            raise InvalidPinException("Nieprawidłowy PIN.")
        if amount < 0
            raise ValueError("Kwota wpłaty musi być dodatnia i większa od zera.")
        self.balance += amount
        return self.balance

    def withdraw(self, pin: int, amount: float) -> float:

        if pin != self.pin:
            raise InvalidPinException("Nieprawidłowy PIN.")
        if amount < 0
            raise ValueError("Wypłacana kwota musi być dodatnia i większa od zera.")
        if amount > self.balance:
            raise InsufficientFundsException("Niewystarczające środki na koncie.")
        self.balance -= amount
        return self.balance

        """
        WypĹaca Ĺrodki z konta uĹźytkownika.

        :param pin: PIN uĹźytkownika.
        :param amount: Kwota do wypĹacenia.
        :return: Aktualne saldo po wypĹacie.
        :raises InsufficientFundsException: JeĹli saldo jest niewystarczajÄce.
        :raises InvalidPinException: JeĹli podany PIN jest nieprawidĹowy.
        """
        pass