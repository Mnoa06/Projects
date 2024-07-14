# # Number Guessing Game
print("This is a guessing Game")
import random
# target_number = random.randint(1,100)
# guess = None
#
# while guess != target_number:
#     guess = int(input("Guess a number between 1 and 100: "))
#     if guess < target_number:
#         print("Too low! Try again")
#     elif guess > target_number:
#         print("Too high! Try again.")
#     else:
#         print("Congrats! you guessed the correct number. ")

target_num = random.randint(1,20)
guess_num = None

while guess_num != target_num:
    guess_num = int(input("Guess a number between 1 and 20: "))
    if guess_num < target_num:
        print("Too low! Try again ")
    elif guess_num > target_num:
        print("Too high! Try again ")
    else:
        print("Congrats! you guessed correctly ")
    

# Factorial calculator with while loop
#Implement a program that calculates the factorial of a given using a "while" loop
print("Factorial calculator")
num = int(input("Enter a number: "))
# factorial is initialized to some starting value
factorial = 1
i = 1

while i <= num:
    # factorial = factorial * i
    factorial *= i
    print(factorial)
    # i = i + 1
    i += 1

print(f"The factorial of {num} is {factorial}")

# Palindrome Checker with While Loop
print("Palindrome Checker")
#Get input from the user
word = input("Enter a word: ")

#initialize variables for checking palindromes
is_palindrome = True
i,j = 0, len(word) - 1

# While the first index is less than the last index
while i > j:
    # Check if the characters at indices i and j are not equal
    if word[i] != word[j]:
        # If not equal, set is_palindrome to Falsoe and exit the loop
        is_palindrome = False
        break
    
    #Move the indices towards the center of the word
    i += 1
    j -= 1
    
if is_palindrome:
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome")
    
#Sum of digits
# Write a porgram that calculates the sum of the digits of a give number using a "while" loop
print("Sum of digits")
num = int(input("Enter a number: "))
digit_sum = 0

while num > 0:
    #This expression calculates the remainder when num is divided by 10. 
    # It effectively extracts the last digit of the number.
    # It adds the last digit to the digit_sum variable. This is a 
    # shorthand notation for updating the variable. It's 
    # equivalent to writing digit_sum = digit_sum + num % 10.
    digit_sum += num %10
    # num //= 10: This is an in-place floor division operation that updates the value of num by 
    # removing the last digit (the remainder when dividing by 10).
    # Example: If num is 123, then num //= 10 updates num to 12 by removing the last digit.
    num //= 10
    
    print(f"The sum of the digits is {digit_sum}")
    
    
    # Interactive Calculator
    # Create a simple calculator that can perform basic operations(+,-,*,/) based on the user input using a while loop
print("This is an iteractive calculator")
while True:
    print("Selection operation: ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter a choice (1-5): ")

    if choice  == "5":
        print("Exiting the calculator.")
        break
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        print(f"{num1} + {num2} = {num1 + num2}")
    elif choice == "2":
        print(f"{num1} - {num2} = {num1 - num2}")
    elif choice == "3":
        print(f"{num1} * {num2} = {num1 * num2}")
    elif choice == "4":
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Cannot divide by zero. Please enrer a non-zero second number")
    else:
        print("Invalid input. Please enter a number between 1 and 5.")
            
# Grade Calculator
# Create a program that takes a student'sscore as input as input and outputs their corresponding letter grade.

print("Grade Calculator")
score = float(input("Enter a student's score: "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
    
print(f"The student's grade is {grade}")

# Number Comparison
# Write a program that compares two numbers and prints 
# whether they are equal, greater, or smaller.
print("Number Comparison")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 == num2:
    print("Both numbers are equal.")
elif num1 > num2:
    print(f"{num1} is greater than {num2}.")
else:
    print(f"{num1} is smaller than {num2}.")


#Leap Year Checker
print("Leap Year Checker")
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
    
#Positive/Negative/Zero Checker
# Write a program that checks whether a given number is positive, negative, or zero.
print("Positive/Negative/Zero Checker")
num = float(input("Enter a number: "))

if num > 0:
    print("The number is positive.")

elif num < 0:
    print("The number is negative.")

else:
    print("The number is zero.")
    
    
#Even/Odd Number Checker:
print("Even/Odd Number Checker")

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
    
print()
print("Even/Odd Number Checker")

num3 = float(input("Enter the first number: "))
num4 = float(input("Enter the second number: "))

if num3 == num4:
    print("Both numbers are equal.")
elif num3 > num4:
    print(f"{num3} is the greater than {num4}")
else:
    print(f"{num3} is smaller than {num4}")

#Leap Year Checker
#Implement a program that checks whether a given year is a leap year.
print("Leap Year Checker")
year = int(input("Enter a year: "))

if (year % 4 == 0 and year %100 !=0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year")

#Positive/Negative/Zero Checker
#Write a program that checks whether a given is positive, negative, or zero
print()
print("Positive/Negative/Zero Checker")
num = float(input("Enter a numbher: "))

if num > 0:
    print("The number is positive.")
if num < 0:
    print("The number is negative.")
else:
    print("The number is zero.") 
    
#Even/Odd Checker
print("Even/Odd Checker")
number = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


