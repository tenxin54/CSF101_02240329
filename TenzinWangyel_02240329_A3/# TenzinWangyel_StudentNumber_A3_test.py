import unittest
from TenzinWangyel_StudentNumber_A3 import Bank, BankAccount, InvalidInputError, InsufficientFundsError, AccountNotFoundError

class TestBankAccount(unittest.TestCase):
    """Tests for BankAccount class"""
    
    def setUp(self):
        self.account = BankAccount("123", "John Doe", 100.0)
    
    def test_deposit_valid(self):
        self.account.deposit(50)
        self.assertEqual(self.account.balance, 150.0)
    
    def test_deposit_invalid(self):
        with self.assertRaises(InvalidInputError):
            self.account.deposit(-10)
    
    def test_withdraw_valid(self):
        self.account.withdraw(50)
        self.assertEqual(self.account.balance, 50.0)
    
    def test_withdraw_invalid_amount(self):
        with self.assertRaises(InvalidInputError):
            self.account.withdraw(-10)
    
    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(InsufficientFundsError):
            self.account.withdraw(200)

class TestBank(unittest.TestCase):
    """Tests for Bank class"""
    
    def setUp(self):
        self.bank = Bank()
        self.bank.create_account("001", "Alice", 200.0)
        self.bank.create_account("002", "Bob", 300.0)
    
    def test_create_duplicate_account(self):
        with self.assertRaises(InvalidInputError):
            self.bank.create_account("001", "Charlie")
    
    def test_valid_deposit(self):
        self.bank.deposit("001", 50)
        self.assertEqual(self.bank.get_account("001").balance, 250.0)
    
    def test_deposit_invalid_account(self):
        with self.assertRaises(AccountNotFoundError):
            self.bank.deposit("003", 100)
    
    def test_valid_withdraw(self):
        self.bank.withdraw("001", 50)
        self.assertEqual(self.bank.get_account("001").balance, 150.0)
    
    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(InsufficientFundsError):
            self.bank.withdraw("001", 300)
    
    def test_valid_transfer(self):
        self.bank.transfer("001", "002", 100)
        self.assertEqual(self.bank.get_account("001").balance, 100.0)
        self.assertEqual(self.bank.get_account("002").balance, 400.0)
    
    def test_transfer_invalid_account(self):
        with self.assertRaises(AccountNotFoundError):
            self.bank.transfer("001", "003", 50)
    
    def test_delete_account(self):
        self.bank.delete_account("001")
        with self.assertRaises(AccountNotFoundError):
            self.bank.get_account("001")
    
    def test_mobile_top_up(self):
        result = self.bank.top_up_mobile("001", "555-1234", 50)
        self.assertEqual(result, "$50.00 topped up to 555-1234")
        self.assertEqual(self.bank.get_account("001").balance, 150.0)
    
    def test_display_all_accounts(self):
        output = self.bank.display_all_accounts()
        self.assertIn("Account: 001", output)
        self.assertIn("Account: 002", output)

if __name__ == "__main__":
    unittest.main()