import unittest
from src.atm import ATM, InvalidPinException, InsufficientFundsException

class ATMTestCase(unittest.TestCase):
    def setUp(self):
        self.atm = ATM(pin=1234, balance=1000)
        def test_deposit_should_increase_balance(self):
        self.atm.deposit(1234, 500)
        self.assertEqual(self.atm.check_balance(1234), 1500)
    
    def test_withdraw_should_decrease_balance(self):
        result = self.atm.withdraw(1234, 300)
        self.assertEqual(self.atm.check_balance(1234), 700)
    
    def test_withdraw_should_fail_if_insufficient_funds(self):
        with self.assertRaises(InsufficientFundsException):
            self.atm.withdraw(1234, 2000)
        self.assertEqual(self.atm.check_balance(1234), 1000)
    
    def test_deposit_negative_amount_should_fail(self):
        with self.assertRaises(ValueError):
            self.atm.deposit(1234, -100)
        self.assertEqual(self.atm.check_balance(1234), 1000)
    
    def test_withdraw_negative_amount_should_fail(self):
        with self.assertRaises(ValueError):
            self.atm.withdraw(1234, -200)
        self.assertEqual(self.atm.check_balance(1234), 1000)
    
    def test_get_balance_should_return_correct_amount(self):
        self.assertEqual(self.atm.check_balance(1234), 1000)
    
    def test_invalid_pin_should_raise_exception(self):
        with self.assertRaises(InvalidPinException):
            self.atm.check_balance(9999)
    
    def test_invalid_pin_on_withdraw_should_raise_exception(self):
        with self.assertRaises(InvalidPinException):
            self.atm.withdraw(9999, 100)
    
    def test_invalid_pin_on_deposit_should_raise_exception(self):
        with self.assertRaises(InvalidPinException):
            self.atm.deposit(9999, 100)
    
    def test_withdraw_all_funds_should_leave_zero_balance(self):
        self.atm.withdraw(1234, 1000)
        self.assertEqual(self.atm.check_balance(1234), 0)

if __name__ == '__main__':
    unittest.main()
