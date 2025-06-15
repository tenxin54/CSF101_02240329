import tkinter as tk
from tkinter import messagebox, simpledialog

# Custom exception classes
class InvalidInputError(Exception):
    """Raised when user input is invalid"""
    pass

class InsufficientFundsError(Exception):
    """Raised when account has insufficient funds"""
    pass

class AccountNotFoundError(Exception):
    """Raised when account doesn't exist"""
    pass

class BankAccount:
    """Represents a bank account with basic operations"""
    
    def __init__(self, account_number, name, balance=0.0):
        """
        Initialize a bank account
        
        Args:
            account_number (str): Account ID
            name (str): Account holder name
            balance (float): Starting balance
        """
        self.account_number = account_number
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        """Add money to account balance"""
        if amount <= 0:
            raise InvalidInputError("Deposit amount must be positive")
        self.balance += amount
    
    def withdraw(self, amount):
        """Deduct money from account balance"""
        if amount <= 0:
            raise InvalidInputError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds")
        self.balance -= amount
    
    def display(self):
        """Return formatted account information"""
        return f"Account: {self.account_number}\nName: {self.name}\nBalance: ${self.balance:.2f}"

class Bank:
    """Manages multiple bank accounts and operations"""
    
    def __init__(self):
        self.accounts = {}
    
    def create_account(self, account_number, name, initial_balance=0.0):
        """Create a new bank account"""
        if account_number in self.accounts:
            raise InvalidInputError("Account number already exists")
        self.accounts[account_number] = BankAccount(account_number, name, initial_balance)
    
    def deposit(self, account_number, amount):
        """Deposit money into specified account"""
        account = self.get_account(account_number)
        account.deposit(amount)
    
    def withdraw(self, account_number, amount):
        """Withdraw money from specified account"""
        account = self.get_account(account_number)
        account.withdraw(amount)
    
    def transfer(self, from_account, to_account, amount):
        """Transfer money between accounts"""
        source = self.get_account(from_account)
        target = self.get_account(to_account)
        source.withdraw(amount)
        target.deposit(amount)
    
    def delete_account(self, account_number):
        """Remove an account from the bank"""
        if account_number not in self.accounts:
            raise AccountNotFoundError("Account not found")
        del self.accounts[account_number]
    
    def top_up_mobile(self, account_number, phone_number, amount):
        """Top up mobile phone balance from bank account"""
        account = self.get_account(account_number)
        account.withdraw(amount)
        return f"${amount:.2f} topped up to {phone_number}"
    
    def get_account(self, account_number):
        """Retrieve account by number"""
        if account_number not in self.accounts:
            raise AccountNotFoundError("Account not found")
        return self.accounts[account_number]
    
    def display_all_accounts(self):
        """Get information for all accounts"""
        if not self.accounts:
            return "No accounts found"
        return "\n\n".join(acc.display() for acc in self.accounts.values())

class BankGUI:
    """Graphical user interface for banking application"""
    
    def __init__(self, bank):
        self.bank = bank
        self.root = tk.Tk()
        self.root.title("Banking System")
        self.root.geometry("500x500")
        
        # Create main frame
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(pady=20)
        
        # Create buttons
        self.create_widgets()
        
        # Output area
        self.output_text = tk.Text(self.root, height=15, width=60)
        self.output_text.pack(pady=10)
        self.output_text.config(state=tk.DISABLED)
    
    def create_widgets(self):
        """Create interface buttons"""
        buttons = [
            ("Create Account", self.create_account),
            ("Deposit", self.deposit),
            ("Withdraw", self.withdraw),
            ("Transfer", self.transfer),
            ("Top Up Mobile", self.top_up_mobile),
            ("Delete Account", self.delete_account),
            ("Display All", self.display_all),
            ("Exit", self.root.quit)
        ]
        
        for text, command in buttons:
            tk.Button(
                self.main_frame, 
                text=text, 
                width=15,
                command=command
            ).pack(side=tk.LEFT, padx=5)
    
    def get_input(self, prompt):
        """Get user input through dialog"""
        return simpledialog.askstring("Input", prompt)
    
    def show_output(self, message):
        """Display message in output area"""
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, message)
        self.output_text.config(state=tk.DISABLED)
    
    def create_account(self):
        """Handle account creation"""
        try:
            acc_num = self.get_input("Enter account number:")
            name = self.get_input("Enter account holder name:")
            self.bank.create_account(acc_num, name)
            self.show_output(f"Account {acc_num} created for {name}")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def deposit(self):
        """Handle deposit operation"""
        try:
            acc_num = self.get_input("Enter account number:")
            amount = float(self.get_input("Enter deposit amount:"))
            self.bank.deposit(acc_num, amount)
            self.show_output(f"Deposited ${amount:.2f} to account {acc_num}")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def withdraw(self):
        """Handle withdrawal operation"""
        try:
            acc_num = self.get_input("Enter account number:")
            amount = float(self.get_input("Enter withdrawal amount:"))
            self.bank.withdraw(acc_num, amount)
            self.show_output(f"Withdrew ${amount:.2f} from account {acc_num}")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def transfer(self):
        """Handle funds transfer"""
        try:
            from_acc = self.get_input("Transfer from account:")
            to_acc = self.get_input("Transfer to account:")
            amount = float(self.get_input("Enter transfer amount:"))
            self.bank.transfer(from_acc, to_acc, amount)
            self.show_output(f"Transferred ${amount:.2f} from {from_acc} to {to_acc}")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def top_up_mobile(self):
        """Handle mobile top-up"""
        try:
            acc_num = self.get_input("Enter account number:")
            phone = self.get_input("Enter phone number:")
            amount = float(self.get_input("Enter top-up amount:"))
            result = self.bank.top_up_mobile(acc_num, phone, amount)
            self.show_output(result)
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def delete_account(self):
        """Handle account deletion"""
        try:
            acc_num = self.get_input("Enter account number to delete:")
            self.bank.delete_account(acc_num)
            self.show_output(f"Account {acc_num} deleted")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def display_all(self):
        """Display all accounts"""
        try:
            self.show_output(self.bank.display_all_accounts())
        except Exception as e:
            messagebox.showerror("Error", str(e))

# Main execution
if __name__ == "__main__":
    bank = Bank()
    gui = BankGUI(bank)
    gui.root.mainloop()