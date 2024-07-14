#Squared Numbers 
#Generate a list of squared numbers from 1 to 10 using list comprehension
print("Squared Numbers")
squared_numbers  = [x**2 for x in range(1,11)]
print(squared_numbers)

#Even Numbers
#Create a list of even numbers from 1 to 20 using list comprehentsion
print()
print("Even Numbers")
even_numbers  = [x for x in range(1,21) if x % 2 == 0]
print(even_numbers)
print("Next Question")

#Vowel Counter
#Count the number of vowels in a given word using list comprehension

word = "programming"
vowel_count = len([char for char in word if char.lower() in "aeiou"])
print(f"The number of vowels in '{word}' is {vowel_count}")

print()
print("Words with legnth 5")
#Words with length 5:
words = [ "apple", "banana", "orange", "grape", "kiwi"]
words_length_5 = [word for word in words if len(word) == 5]
print(words_length_5)


