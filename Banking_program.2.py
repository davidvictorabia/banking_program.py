# Banking_program
# A simple banking program that allows users to create accounts, deposit and withdraw money, 
# and check their balance. Now with PIN protection, multiple accounts, and transaction history.

import datetime

class BankAccount:
    def __init__(self, account_name, pin):
        self.account_name = account_name
        self.pin = pin
        self.balance = 0.00
        self.transaction_history = []
    
    def show_balance(self):
        print("******************************")
        print(f"Account: {self.account_name}")
        print(f"Your current balance is: ${self.balance:.2f}")
        print("******************************")
    
    def deposit(self):
        print("******************************")
        try:
            amount = float(input("Enter the amount to deposit: $"))
            print("******************************")
            if amount < 0:
                print("*****************************")
                print("Invalid amount. Please enter a positive number.")
                print("*****************************")
                return 0
            elif amount == 0:
                print("*****************************")
                print("Please enter an amount greater than zero.")
                print("*****************************")
                return 0
            else:
                self.balance += amount
                self.transaction_history.append({
                    'type': 'Deposit',
                    'amount': amount,
                    'date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'balance_after': self.balance
                })
                print(f"Successfully deposited ${amount:.2f}")
                return amount
        except ValueError:
            print("*****************************")
            print("Invalid input. Please enter a valid number.")
            print("*****************************")
            return 0
    
    def withdraw(self):
        print("**********************************")
        try:
            amount = float(input("Enter the amount to withdraw: $"))
            print("**********************************")
            if amount < 0:
                print("******************************")
                print("Invalid amount. Please enter a positive number.")
                print("******************************")
                return 0
            elif amount > self.balance:
                print("Insufficient funds. Please try again.")
                return 0
            elif amount == 0:
                print("******************************")
                print("Please enter an amount greater than zero.")
                print("******************************")
                return 0
            else:
                self.balance -= amount
                self.transaction_history.append({
                    'type': 'Withdrawal',
                    'amount': amount,
                    'date': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'balance_after': self.balance
                })
                print(f"Successfully withdrew ${amount:.2f}")
                return amount
        except ValueError:
            print("*****************************")
            print("Invalid input. Please enter a valid number.")
            print("*****************************")
            return 0
    
    def show_transaction_history(self):
        print("=" * 50)
        print(f"Transaction History for {self.account_name}")
        print("=" * 50)
        if not self.transaction_history:
            print("No transactions yet.")
        else:
            for i, transaction in enumerate(self.transaction_history, 1):
                print(f"{i}. [{transaction['date']}] {transaction['type']}: ${transaction['amount']:.2f}")
                print(f"   Balance after: ${transaction['balance_after']:.2f}")
        print("=" * 50)


class Bank:
    def __init__(self):
        self.accounts = {}
    
    def create_account(self):
        print("==================================")
        print("------ Create New Account --------")
        print("==================================")
        account_name = input("Enter account name: ")
        
        if account_name in self.accounts:
            print("Account already exists!")
            return None
        
        pin = input("Create a 4-digit PIN: ")
        if len(pin) != 4 or not pin.isdigit():
            print("PIN must be exactly 4 digits.")
            return None
        
        confirm_pin = input("Confirm your PIN: ")
        if pin != confirm_pin:
            print("PINs do not match.")
            return None
        
        self.accounts[account_name] = BankAccount(account_name, pin)
        print(f"Account '{account_name}' created successfully!")
        return account_name
    
    def get_account(self, account_name, pin):
        if account_name in self.accounts:
            if self.accounts[account_name].pin == pin:
                return self.accounts[account_name]
            else:
                print("Incorrect PIN.")
        else:
            print("Account not found.")
        return None
    
    def login(self):
        print("==================================")
        print("------------ Login ---------------")
        print("==================================")
        account_name = input("Enter account name: ")
        
        if account_name not in self.accounts:
            print("Account not found.")
            return None
        
        attempts = 0
        max_attempts = 3
        
        while attempts < max_attempts:
            pin = input("Enter PIN: ")
            account = self.get_account(account_name, pin)
            if account:
                print(f"Welcome back, {account_name}!")
                return account
            else:
                attempts += 1
                print(f"Incorrect PIN. {max_attempts - attempts} attempts remaining.")
        
        print("Too many failed attempts. Returning to main menu.")
        return None


def main():
    bank = Bank()
    # Create a default account for testing
    bank.accounts["test"] = BankAccount("test", "1234")
    
    is_running = True
    current_account = None

    while is_running:
        if current_account is None:
            print("\n=====================================")
            print("----- Welcome to the Banking Program! -----")
            print("===========================================")
            print("1. Login to existing account")
            print("2. Create new account")
            print("3. Exit")
            print("-----------------------------------")
            choice = input("Please select an option (1-3): ")
        
            if choice == "1":
                current_account = bank.login()
            elif choice == "2":
                bank.create_account()
            elif choice == "3":
                is_running = False
            else:
                print("Invalid option. Please try again.")
        else:
            print("\n=====================================")
            print(f"---- Welcome, {current_account.account_name}! ----")
            print("=====================================")
            print("1. Show Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Transaction History")
            print("5. Switch Account")
            print("6. Exit")
            print("-----------------------------------")
            choice = input("Please select an option (1-6): ")
        
            if choice == "1":
                current_account.show_balance()
            elif choice == "2":
                current_account.deposit()
            elif choice == "3":
                current_account.withdraw()
            elif choice == "4":
                current_account.show_transaction_history()
            elif choice == "5":
                current_account = None
                print("Logged out successfully.")
            elif choice == "6":
                is_running = False
            else:
                print("Invalid option. Please try again.")
    
    print("\n=====================================")
    print("Thank you for banking with us!")
    print("=====================================")


if __name__ == '__main__':
    main()
