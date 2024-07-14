#Simple Bank Account
#Create a "BankAccount" class with methods doe deposit,withdraw, and check balance

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    
    def deposit(self,amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")
        
        
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw ${amount}. New balance: ${self.balance}")
        
        else:
            print("Insufficient funds")
    def check_balance(self):
        print(f"Current balance: ${self.balance}")
        
#Example usage:
account = BankAccount()
account.check_balance()
account.deposit(100)
account.check_balance()
account.deposit(200)
account.check_balance()
account.withdraw(30)
account.check_balance
print()
print()
print()
#Student Info System
#Create a "student" class with methods to set and display student information

class Student:
    def __init__ (self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def set_information(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        
    def display_information(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")
        
student = (Student("Marven", 35, "A"))
student.display_information()
student.set_information("Marvin", 25, "B")
student.display_information()
    

print()

#Book Library
#Create a "book" class with methods for lending and returning books.
print()

class Book:
    def __init__(self, title, author, available = True):
        self.title = title
        self.author = author
        self.available = available
        
    def lend_book(self):
        if self.available:
            self.available = False
            print(f"The book '{self.title}' by {self.author} has been lent ")
        else:
            print("Sorry, the book is currently available. ")
    
    def return_book(self):
        if not self.available:
            self.available = True
            print(f"Thank you for returning '{self.title}' by {self.author}.") 
        else:
            print("The book is already available")

#example usage
book1 = Book("The Catcher in the Rye", "J.D. Salinger")
book2 = Book("Math Book", "Mathetician")
print(book1.title)
print(book2.title)
print()
book1.lend_book()
print()
book1.lend_book()
print()
book1.return_book()

# Temperature converter
# Create a TemperatureConverter class with methods to
# convert Celsius to Fahrenheit and vice versa.

class TempConverter:
    def celsius_to_fahrenheit(self, celsius):
        print(celsius)
        return (celsius * 9/5) + 32
    
    def fahrenheit_to_celsius(self,fahrenheit):
        print(fahrenheit)
        return (fahrenheit -32) * 5/9
    
#Example usage
converter = TempConverter()
print(converter.celsius_to_fahrenheit(25))
print()
print(converter.fahrenheit_to_celsius(77))

class Car:
    def __init__ (self):
        self.speed = 0 
        
    def start(self):
        print("Car started. Reay to go!")
        
    def stop(self):
        print("Car stopped. Have a safe journey!")
    
    def accelerate(self, speed_increase):
        self.speed += speed_increase
        print(f"Accelerated. Current speed: {self.speed} km/h")
        
    def brake(self, speed_decrease):
        if self.speed >= speed_decrease:
            self.speed -= speed_decrease
            print(f"Braked. Current speed: {self.speed} km/h")
            
        else:
            print("Car cannot go below 0 km/h. stopping")
            
            
car = Car()
car.start()
car.accelerate(25)
car.brake(20)
car.stop

