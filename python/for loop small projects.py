# Create a program that takes a number as input and generates its multiplication table up to a specified range
#Multiplication Table Generator

# num = int(input("Enter a number: "))
# for i in range(1,11):
#     print(f"{num} x {i} = {num * i}")
#
# num = int(input("Enter a number: "))
# for i in range(1,11):
#     print(f"{num} x {i} = {num * i}")

# Number Pyramid
# Write a program to print a number pyramid pattern using nested for loops


n = int(input("Enter the number of rows: "))
for i in range(1, n+ 1):
    for j in range(1, i + 1):
        print(j, end= " ")
    print()
    
#Factorial Calculator:
#Create a program that calculates the factorial of a given number using a 'for' loop.

num = int(input("Enter a number: "))
factorial = 1
for i in range (1, num + 1):
    factorial *= i
    print(factorial)
print(f"The facortial of {num} is {factorial}")

#Simple To-Do List
# Implement a  simple to-do list program that allows users to add tasks and then prints the tasks using a 'for' loop

tasks = []
n = int(input("Enter the number of tasks: "))
for i in range(n):
    task= input(f"Enter task {i + 1}: ")
    tasks.append(task)
    
print("\nYour To-Do List")
for i,task in enumerate(tasks,start=1):
    print(f"{i}.{task}")

task = []
n = int(input("Enter the number of tasks: "))
for i in range(n):
    task = input(f"")
        

#Palindrome Checker:
#Create a program that checks if a given word is a plaindromeusing a "for" loop

word = input("Enter a word: ")
is_palindrome = True
#This is often used when checking for palindromes because,
# in a palindrome, you only need to compare the characters up to the middle of the string with the 
# characters from the middle to the end (or vice versa).
for i in range(len(word) // 2):
    if word[i] != word[-i -1]:
        is_palindrome = False
        break
    
if is_palindrome:
    print(f"{word} is a palindrome")
    
else:
    print(f"{word} is not a palindrome")
    
