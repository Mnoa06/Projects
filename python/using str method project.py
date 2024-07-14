#Using __str__ method

#Person class with __str__
#Create a Person class w/ attributes for name and age. implement __str__ method to display information about the person

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age  = age
        
    def __str__(self):
        return f"Person: {self.name}, Age: {self.age}"
    
#Example usage
person = Person("Alice", 25)
print(person)


#Book class w/ __str__
#Create a book vlass w/ attributes for the title and author. implement the __str__ method to dispaly info about the book
print()

class Book():
    def __init__(self, title, author):
        self.title = title
        self.author  = author
    
    def __str__(self):
        return f"Book: {self.title} by {self.author}"
    
#example usuage
book = Book("The Cather in the Rye", "J.D. Salinger")
print(book)

print()
#Rectangle class w/ __str__
#Create a Rectangle class w/ attributes for length and width. Implement the __str__ method to display info about the rectangle

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def __str__(self):
        return f"Rectangle: Length = {self.length}, Width = {self.width}"
    
rectangle = Rectangle(5,8)
print(rectangle)

#Employee class w/ __str__:
#Create an Employee class w/ attributes for name and job title. Implement 
#__str__ method to display info about the employee

class Employee:
    def __init__(self, name , job_title):
        self.name = name
        self.job_title = job_title
        
    def __str__(self):
        return f"Employee {self.name}, Job Title: {self.job_title}"

employee  = Employee("Marven", "MRI Tech")
print(employee)