# TenzinWangyel_StudentNumber_A3.py

"""
Simple Banking App with Tkinter UI and Exception Handling
"""

import tkinter as tk

# Custom exception classes
class InvalidInputError(Exception):
    """Raised when the user enters invalid input."""
    pass

class TransferError(Exception):
    """Raised when a transfer cannot be completed."""
    pass

class Account:
    """A simple bank account class."""

    def __init__(self, name, balance=0, phone=""):
        self.name = name
        self.balance = balance
        self.phone = phone

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidInputError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0 or amount > self.balance:
            raise InvalidInputError("Invalid withdrawal amount.")
        self.balance -= amount

    def transfer(self, other_account, amount):
        if amount <= 0 or amount > self.balance:
            raise TransferError("Transfer amount invalid or exceeds balance.")
        self.balance -= amount
        other_account.balance += amount

    def top_up_phone(self, amount):
        if amount <= 0 or amount > self.balance:
            raise InvalidInputError("Invalid top-up amount.")
        self.balance -= amount
        return f"Phone number {self.phone} topped up with {amount}"

    def __str__(self):
        return f"{self.name} - Balance: {self.balance}"

def processUserInput(choice):
    """Processes user menu input."""
    if choice == '1':
        name = input("Enter name: ")
        accounts[name] = Account(name)
        print("Account created.")
    elif choice == '2':
        name = input("Enter name: ")
        amount = float(input("Enter amount to deposit: "))
        accounts[name].deposit(amount)
        print("Deposited.")
    elif choice == '3':
        name = input("Enter name: ")
        amount = float(input("Enter amount to withdraw: "))
        accounts[name].withdraw(amount)
        print("Withdrawn.")
    elif choice == '4':
        name1 = input("Sender name: ")
        name2 = input("Receiver name: ")
        amount = float(input("Enter amount to transfer: "))
        accounts[name1].transfer(accounts[name2], amount)
        print("Transferred.")
    elif choice == '5':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        accounts[name].phone = phone
        amount = float(input("Enter amount to top up: "))
        msg = accounts[name].top_up_phone(amount)
        print(msg)
    elif choice == '6':
        for acc in accounts.values():
            print(acc)
    elif choice == '0':
        print("Goodbye!")
        return False
    else:
        print("Invalid input.")
    return True

# Dictionary to hold accounts
accounts = {}

# CLI main loop
def main():
    while True:
        print("\n1. Create Account\n2. Deposit\n3. Withdraw\n4. Transfer\n5. Top-Up Phone\n6. Show All Accounts\n0. Exit")
        choice = input("Enter choice: ")
        try:
            if not processUserInput(choice):
                break
        except Exception as e:
            print("Error:", e)

# GUI class
class BankingApp:
    def __init__(self, root):
        self.root = root
        root.title("Simple Banking App")

        self.label = tk.Label(root, text="Enter Command (1-6):")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.button = tk.Button(root, text="Submit", command=self.run_command)
        self.button.pack()

        self.output = tk.Text(root, height=10, width=50)
        self.output.pack()

    def run_command(self):
        choice = self.entry.get()
        try:
            if not processUserInput(choice):
                self.root.quit()
        except Exception as e:
            self.output.insert(tk.END, f"Error: {e}\n")

# Run both CLI and GUI
if __name__ == "__main__":
    main()
    # GUI start (optional to comment out if not needed)
    root = tk.Tk()
    app = BankingApp(root)
    root.mainloop()