# TenzinWangyel_StudentNumber_A3_test.py

import unittest
from TenzinWangyel_StudentNumber_A3 import Account, InvalidInputError, TransferError

class TestBankingApp(unittest.TestCase):

    def setUp(self):
        self.acc1 = Account("Alice", 100, "1234567890")
        self.acc2 = Account("Bob", 50)

    def test_deposit_negative(self):
        with self.assertRaises(InvalidInputError):
            self.acc1.deposit(-50)

    def test_withdraw_excess(self):
        with self.assertRaises(InvalidInputError):
            self.acc1.withdraw(150)

    def test_transfer_invalid(self):
        with self.assertRaises(TransferError):
            self.acc1.transfer(self.acc2, 200)

    def test_top_up_invalid(self):
        with self.assertRaises(InvalidInputError):
            self.acc1.top_up_phone(200)

    def test_successful_transfer(self):
        self.acc1.transfer(self.acc2, 30)
        self.assertEqual(self.acc1.balance, 70)
        self.assertEqual(self.acc2.balance, 80)

    def test_successful_top_up(self):
        message = self.acc1.top_up_phone(20)
        self.assertIn("Phone number", message)
        self.assertEqual(self.acc1.balance, 80)

if __name__ == '__main__':
    unittest.main()
