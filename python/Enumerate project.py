#print index and element od a lsit
#Create a program that prints the index and element of element of each item in alist

fruits  = ["apple", "banana", "orange"]
for index,fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")
    

print()
#Character Counter:
#Create a program that counts and prints the number of occurences of each
#character in a string using "enumurate".

text = "Programming"

char_count = {}
for index, char in enumerate(text):
    char_count[char] = char_count.get(char, 0) + 1
    
print("Character counts: ")
for char, count in char_count.items():
    print(f"Character: {char}, Count: {count}")

print()

    
#List Reverser with Index:
#Create a program that reverses a list using "enumerate" to swap element based on their indices

numbers = [1,2,3,4,5]

for i, num  in enumerate(range(len(numbers) // 2)):
    #Swap elements at opposite ends of the list
    numbers[i], numbers[-i - 1] = numbers[-i -1], numbers[i]
    
print("Reversed list: ",numbers)

print()
#Task list with index
#Create a program that prints a numbered list of tasks and allows the user to mark tasks as completed

tasks = ["Read a book", "Write code", "Exercise"]

for index, task in enumerate(tasks, start =1):
    print(f"{index}. {task}")
    
completed_task_index = int(input("Enter the index of the completed task (0 to exit): "))
while completed_task_index != 0:
    tasks[completed_task_index - 1] += "(Completed)"
    for index, task in enumerate(task, start =1):
        print(f"{index}. {task}")
    completed_task_index = int(input("Enter the index of the completed task (0 to exit): "))
    
