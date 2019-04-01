# Palindrome Challenge By Morgan Wells

# Input: User enters a word that they want to know if its a palindrome (entry of word)
# Output: 1) A palindrome ("This is a palindrome") 
#         2) Not a palindrome ("This word is not a pallindrome")
#         3) Error 

# Reference: Reverse a string in Python, (n.d.) Available At: https://stackoverflow.com/questions/931092/reverse-a-string-in-python Accessed: 30-3-19 

# Data Tests:
#           Bad Tests (Not a palindrome): Cat, Nap, hello, goodbye 
#           Good Tests (a palindrome): rotor, Rotor
#           Error (somethings wrong): Hell o
         
# Imported Modules:

import re # This is a module that has a set of commands to help you with regular expressions

# Setting Variables:

input_word = "" # input_word is the variable to store the users word to test

# Getting the user input:

input_word = input("Enter a word: ") # Capturing the word that the user is typing and putting it into the input_word container

# Checking for spaces or non A to Z characters:

pattern = re.compile('[^a-zA-Z]') # Here I am creating a regular expreesion that tests for anything that inst a letter
if (pattern.findall(input_word)):
    print('The word must contain only letters not numbers, spaces or characters')

# Converting all to lowercase letters:

lowercase_word = input_word.lower() # Taking the input_word changing this to lower case and then putting it into the lowercase_ word

# Reversing the input:

reverse_word = lowercase_word[::-1] # Reversing the characters of the word in the string lowercase_word

# Testing to see if input equals reverse of input: 

if (lowercase_word == reverse_word): # Comparing whats in the lowercase_word container and the reverse_word container to see if its a palindrome
    print("This word is a pallindrome")
else: 
    print("This word is not a pallindrome")



