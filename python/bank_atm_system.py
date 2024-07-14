# Create a new Python file (e.g., bank_atm_system.py).
# Define the Person class with attributes (name and age).
# Define the Person Class (Abstraction)
class Person:
    def __init__(self, first_name, last_name, age, ssn_last_four):
        self.first_name = first_name
        self.last_name  = last_name
        self.age = age
        self.ssn_last_four = ssn_last_four

#Define the BankAccount Class (Inheritance, Encapsulation)
# Create the BankAccount class that inherits from Person.
# Add attributes (account_number, balance, password) for the bank account.
# Include methods for deposit, withdraw, transfer, and password verification.

import random

class BankAccount(Person):
    def __init__(self, first_name, last_name, age, ssn_last_four):
        super().__init__(first_name, last_name, age, ssn_last_four)
        self.account_number = self.generate_account_number()
        self.balance = 0
        self.password = None
    
    def generate_account_number(self):
        return random.randint(10000000, 99999999)
    
    def set_password(self, password):
        self.password = password
        
    def verify_password(self, entered_password):
        return self.password == entered_password
    
    def deposit(self,amount):
        self.balance += amount
        return f"Deposited ${amount}. Current balance: ${self.balance}"
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            return "Insufficient funds. Withdrawal failed"
    def transfer(self, recipient, amount):
        if self.balance >= amount:
            self.balance -= amount
            recipient += amount
            return f"Transferred ${amount} to {recipient.first_name} {recipient.last_name}. Your balance: ${self.balance}"
        else:
            return "Insuffiecient funds. Transer failed"
        
# Define the BankSystem Class (Encapsulation)
# Create the BankSystem class to manage multiple bank accounts.
# Include methods for creating accounts, closing accounts, and checking account balances.

class BankSystem:
    def __init__(self):
        self.accounts = []
        
    def create_account(self, first_name, last_name, age, ssn_last_four):
        new_account = BankAccount(first_name, last_name, age, ssn_last_four)
        self.accounts.append(new_account)
        return new_account
    
    def close_account(self,account):
        self.accounts.remove(account)
        return(f"Account closed for {account.first_name} {account.last_name}")
    
    def check_balance(self,account):
        return (f"Current balance for {account.first_name} {account.last_name} ${account.balance}")
    
#Define the TestBankSystem Class (Unit Testing)   
#reate the TestBankSystem class to perform unit testing.
# Include tests for deposit, withdraw, and transfer functionalities.

import unittest
class TestBankSystem(unittest.TestCase):
    def test_deposit(self):
         account = BankAccount("John", "Doe",38,  "5678")
         account.deposit(100)
         self.assertEqual(account.balance,100)
    
    def test_withdraw(self):
        account = BankAccount("Jane", "Doe", 35, "1234")
        account.deposit(200)
        account.withdraw(50)
        self.assertEqual(account.balance,150)
        
    def test_transfer(self):
        account1 = BankAccount("Alice", "Johnson", 30, "9876")
        account2  = BankAccount("Bob", "Williams",25,  "4321")
        account1.deposit(300)
        account1.trasnfer(account2, 100)
        self.assertEqual(account1.balance,200)
        self.assertEqual(account1.balance,100)
        

#  Implement the Bank ATM System
# Create an instance of the BankSystem.
# Use a while loop for the main ATM menu to create accounts, log in, and perform banking operations.
# Add user-friendly prompts for input.

if __name__ == "__main__":
    bank_system = BankSystem()
    
    while True:
        print("\nWelcome to the Bank ATM System!")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == "1":
            #Create Account
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            age = int(input("Please enter your age: "))
            ssn_last_four = input("Enter the last four digits of your social securty number: ")
            # Create a new account and set a password
            new_account = bank_system.create_account(first_name, last_name, age, ssn_last_four)
            password = input("Set a password for your account: ")
            new_account.set_password(password)
            
            print(f"Account created successfully. Your account number is: {new_account.account_number}")
        
        elif choice == "2":
            #login
            account_number = int(input("Enter your account number: "))
            password = input("Enter your password: ")
            
            #find the account
            current_account = None
            for account in bank_system.accounts:
                if account.account_number  == account_number:
                    current_account = account
                    break
            
            if current_account and current_account.verify_password(password):
                while True:
                    print("\nAccount Options:")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Transfer")
                    print("4. Check Balance")
                    print("5. Close Account")
                    print("6. Logout")
                    
                    account_choice = input("Enter your choice (1/2/3/4/5/6)")
                    
                    if account_choice == "1":
                        #deposit
                        amount = float(input("Enter the deposit amount"))
                        print(current_account.deposit(account))
                    
                    elif account_choice == "2":
                        #withdraw
                        amount = float(input("Enter the withdrawl amount"))
                        print(current_account.withdraw(amount))
                        
                    elif account_choice == "3":
                        #transfer
                        recipient_account_number = int(input("Enter the receipents's account number"))
                        recipient_account = None
                        
                        #Find the recipeient account
                        for account in bank_system.accounts:
                            if account.account_number == recipient_account_number:
                                recipient_account = account
                                break
                        
                        if recipient_account:
                            amount = float(input("Enter the tramsfer amount: "))
                            print(current_account.transfer(recipient_account, amount))
                        else:
                            print("Recipient account not found.") 
                    elif account_choice == "4":
                        #check balance
                       print(bank_system.check_balance(current_account))
                       
                    elif account_choice == "5":
                        #close account
                        print(bank_system.close_account(current_account))
                        break
                    elif account_choice == "6":
                        #logout
                        break
                    
                    else:
                       print("Invalid choice. Please enter a valid option.")
                       
            else:
                print("Login failed. Incorrect account number or password.")
        elif choice == "3":
            # Exit
            print("Thank you for using the Bank ATM System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")                   
                    
