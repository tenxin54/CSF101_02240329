import tkinter as tk
from tkinter import messagebox

class BankAccount:
    """A class representing a basic bank account with common operations."""
    
    def __init__(self, account_number, name, balance=0):
        """
        Initialize a bank account with account number, name, and optional balance.
        
        Args:
            account_number (str): The account number
            name (str): Account holder's name
            balance (float, optional): Initial balance. Defaults to 0.
        """
        self.account_number = account_number
        self.name = name
        self.balance = balance
        self.mobile_balance = 0  # Prepaid mobile balance
    
    def deposit(self, amount):
        """
        Deposit money into the account.
        
        Args:
            amount (float): Amount to deposit
            
        Raises:
            InvalidAmountError: If amount is negative
        """
        if amount <= 0:
            raise InvalidAmountError("Deposit amount must be positive")
        self.balance += amount
        return f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}"
    
    def withdraw(self, amount):
        """
        Withdraw money from the account.
        
        Args:
            amount (float): Amount to withdraw
            
        Raises:
            InvalidAmountError: If amount is negative
            InsufficientFundsError: If balance is insufficient
        """
        if amount <= 0:
            raise InvalidAmountError("Withdrawal amount must be positive")
        if self.balance < amount:
            raise InsufficientFundsError("Insufficient funds for withdrawal")
        self.balance -= amount
        return f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}"
    
    def transfer(self, amount, recipient_account):
        """
        Transfer money to another account.
        
        Args:
            amount (float): Amount to transfer
            recipient_account (BankAccount): The receiving account
            
        Raises:
            InvalidAmountError: If amount is negative
            InsufficientFundsError: If balance is insufficient
        """
        if amount <= 0:
            raise InvalidAmountError("Transfer amount must be positive")
        if self.balance < amount:
            raise InsufficientFundsError("Insufficient funds for transfer")
        self.balance -= amount
        recipient_account.balance += amount
        return f"Transferred ${amount:.2f} to {recipient_account.name}. New balance: ${self.balance:.2f}"
    
    def top_up_mobile(self, amount, phone_number):
        """
        Top up mobile prepaid balance.
        
        Args:
            amount (float): Amount to top up
            phone_number (str): Phone number to credit
            
        Raises:
            InvalidAmountError: If amount is negative
            InsufficientFundsError: If balance is insufficient
        """
        if amount <= 0:
            raise InvalidAmountError("Top-up amount must be positive")
        if self.balance < amount:
            raise InsufficientFundsError("Insufficient funds for mobile top-up")
        self.balance -= amount
        self.mobile_balance += amount
        return f"Topped up ${amount:.2f} to {phone_number}. Mobile balance: ${self.mobile_balance:.2f}. Account balance: ${self.balance:.2f}"
    
    def delete_account(self):
        """Mark the account for deletion and return the remaining balance."""
        remaining_balance = self.balance
        self.balance = 0
        return f"Account deleted. Withdrawn ${remaining_balance:.2f}"

class InvalidAmountError(Exception):
    """Exception raised for invalid amounts (negative or zero)."""
    pass

class InsufficientFundsError(Exception):
    """Exception raised when there are insufficient funds for an operation."""
    pass

class BankingAppGUI:
    """A simple GUI for the banking application."""
    
    def __init__(self, root):
        """
        Initialize the banking application GUI.
        
        Args:
            root (tk.Tk): The root window
        """
        self.root = root
        self.root.title("Simple Banking App")
        
        # Create some sample accounts
        self.accounts = {
            "12345": BankAccount("12345", "John Doe", 1000),
            "67890": BankAccount("67890", "Jane Smith", 500)
        }
        
        self.current_account = None
        
        # Create GUI elements
        self.create_widgets()
    
    def create_widgets(self):
        """Create and arrange all the GUI widgets."""
        # Account selection frame
        account_frame = tk.LabelFrame(self.root, text="Account Selection", padx=10, pady=10)
        account_frame.pack(padx=10, pady=10, fill="x")
        
        tk.Label(account_frame, text="Account Number:").grid(row=0, column=0)
        self.account_entry = tk.Entry(account_frame)
        self.account_entry.grid(row=0, column=1)
        
        self.select_button = tk.Button(account_frame, text="Select Account", command=self.select_account)
        self.select_button.grid(row=0, column=2, padx=5)
        
        # Account info frame
        info_frame = tk.LabelFrame(self.root, text="Account Information", padx=10, pady=10)
        info_frame.pack(padx=10, pady=10, fill="x")
        
        self.info_label = tk.Label(info_frame, text="No account selected", justify="left")
        self.info_label.pack()
        
        # Operations frame
        operation_frame = tk.LabelFrame(self.root, text="Operations", padx=10, pady=10)
        operation_frame.pack(padx=10, pady=10, fill="x")
        
        # Deposit
        tk.Label(operation_frame, text="Amount:").grid(row=0, column=0)
        self.amount_entry = tk.Entry(operation_frame)
        self.amount_entry.grid(row=0, column=1)
        
        self.deposit_button = tk.Button(operation_frame, text="Deposit", command=self.deposit)
        self.deposit_button.grid(row=0, column=2, padx=5)
        
        # Withdraw
        self.withdraw_button = tk.Button(operation_frame, text="Withdraw", command=self.withdraw)
        self.withdraw_button.grid(row=1, column=2, padx=5)
        
        # Transfer
        tk.Label(operation_frame, text="Recipient Account:").grid(row=2, column=0)
        self.recipient_entry = tk.Entry(operation_frame)
        self.recipient_entry.grid(row=2, column=1)
        
        self.transfer_button = tk.Button(operation_frame, text="Transfer", command=self.transfer)
        self.transfer_button.grid(row=2, column=2, padx=5)
        
        # Mobile top-up
        tk.Label(operation_frame, text="Phone Number:").grid(row=3, column=0)
        self.phone_entry = tk.Entry(operation_frame)
        self.phone_entry.grid(row=3, column=1)
        
        self.topup_button = tk.Button(operation_frame, text="Mobile Top-Up", command=self.top_up_mobile)
        self.topup_button.grid(row=3, column=2, padx=5)
        
        # Delete account
        self.delete_button = tk.Button(operation_frame, text="Delete Account", command=self.delete_account)
        self.delete_button.grid(row=4, column=2, padx=5)
        
        # Output frame
        output_frame = tk.LabelFrame(self.root, text="Output", padx=10, pady=10)
        output_frame.pack(padx=10, pady=10, fill="both", expand=True)
        
        self.output_text = tk.Text(output_frame, height=10, state="disabled")
        self.output_text.pack(fill="both", expand=True)
    
    def select_account(self):
        """Select an account based on the entered account number."""
        account_number = self.account_entry.get()
        if account_number in self.accounts:
            self.current_account = self.accounts[account_number]
            self.update_account_info()
            self.append_output(f"Selected account: {self.current_account.name}")
        else:
            messagebox.showerror("Error", "Account not found")
    
    def update_account_info(self):
        """Update the account information display."""
        if self.current_account:
            info = f"Name: {self.current_account.name}\n"
            info += f"Account Number: {self.current_account.account_number}\n"
            info += f"Balance: ${self.current_account.balance:.2f}\n"
            info += f"Mobile Balance: ${self.current_account.mobile_balance:.2f}"
            self.info_label.config(text=info)
        else:
            self.info_label.config(text="No account selected")
    
    def append_output(self, message):
        """Append a message to the output text area."""
        self.output_text.config(state="normal")
        self.output_text.insert("end", message + "\n")
        self.output_text.see("end")
        self.output_text.config(state="disabled")
    
    def process_user_input(self, choice, amount=None, recipient_account=None, phone_number=None):
        """
        Process user input for banking operations.
        
        Args:
            choice (str): The operation to perform
            amount (float, optional): Amount for the operation. Defaults to None.
            recipient_account (BankAccount, optional): Recipient account for transfer. Defaults to None.
            phone_number (str, optional): Phone number for top-up. Defaults to None.
            
        Returns:
            str: Result message of the operation
        """
        if not self.current_account:
            return "No account selected"
        
        try:
            if choice == "deposit":
                return self.current_account.deposit(amount)
            elif choice == "withdraw":
                return self.current_account.withdraw(amount)
            elif choice == "transfer":
                if recipient_account in self.accounts:
                    return self.current_account.transfer(amount, self.accounts[recipient_account])
                else:
                    return "Recipient account not found"
            elif choice == "topup":
                return self.current_account.top_up_mobile(amount, phone_number)
            elif choice == "delete":
                result = self.current_account.delete_account()
                del self.accounts[self.current_account.account_number]
                self.current_account = None
                self.update_account_info()
                return result
            else:
                return "Invalid operation"
        except (InvalidAmountError, InsufficientFundsError) as e:
            return f"Error: {str(e)}"
    
    def deposit(self):
        """Handle deposit operation from GUI."""
        if not self.current_account:
            messagebox.showerror("Error", "No account selected")
            return
        
        try:
            amount = float(self.amount_entry.get())
            result = self.process_user_input("deposit", amount=amount)
            self.append_output(result)
            self.update_account_info()
        except ValueError:
            messagebox.showerror("Error", "Invalid amount")
    
    def withdraw(self):
        """Handle withdrawal operation from GUI."""
        if not self.current_account:
            messagebox.showerror("Error", "No account selected")
            return
        
        try:
            amount = float(self.amount_entry.get())
            result = self.process_user_input("withdraw", amount=amount)
            self.append_output(result)
            self.update_account_info()
        except ValueError:
            messagebox.showerror("Error", "Invalid amount")
    
    def transfer(self):
        """Handle transfer operation from GUI."""
        if not self.current_account:
            messagebox.showerror("Error", "No account selected")
            return
        
        try:
            amount = float(self.amount_entry.get())
            recipient = self.recipient_entry.get()
            result = self.process_user_input("transfer", amount=amount, recipient_account=recipient)
            self.append_output(result)
            self.update_account_info()
        except ValueError:
            messagebox.showerror("Error", "Invalid amount")
    
    def top_up_mobile(self):
        """Handle mobile top-up operation from GUI."""
        if not self.current_account:
            messagebox.showerror("Error", "No account selected")
            return
        
        try:
            amount = float(self.amount_entry.get())
            phone_number = self.phone_entry.get()
            if not phone_number:
                messagebox.showerror("Error", "Please enter a phone number")
                return
            result = self.process_user_input("topup", amount=amount, phone_number=phone_number)
            self.append_output(result)
            self.update_account_info()
        except ValueError:
            messagebox.showerror("Error", "Invalid amount")
    
    def delete_account(self):
        """Handle account deletion from GUI."""
        if not self.current_account:
            messagebox.showerror("Error", "No account selected")
            return
        
        if messagebox.askyesno("Confirm", "Are you sure you want to delete this account?"):
            result = self.process_user_input("delete")
            self.append_output(result)
            self.account_entry.delete(0, "end")

def main():
    """Main function to start the banking application."""
    root = tk.Tk()
    app = BankingAppGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()