# Palindreome Challenge By Morgan Wells

# Input: User enters a word that they want to know if its a palindreome (entry of word)
# Output: 1) A palindreome ("This is a palindreome") 
#         2) Not a palidreome ("This word is not a pallindrome")
#         3) Error 

# References: Reverse a string in Python, Available At: https://stackoverflow.com/ Acessed: 30-3-19 

# Data Tests:
#           Bad Tests (Not a palindreome): Cat, Nap, hello, goodbye 
#           Good Tests (a palindreome): rotor, Rotor
#           Error (somethings wrong): Hell o
         
# import modules

import re # Regular Expressions is a module that has a set of commmands to help you with regular expresssions

# Set Variables

input_word = "" # input_word is the variable to store the users word to test

# Get the user input

input_word = input("Enter a word: ") # capturing the word that the user is typing and putting it into the input_word conatiner

# Check for spaces or non A to Z charceetrs

pattern = re.compile('[^a-zA-Z]') # creating a regular expreesion that tests for anything that isnt a letter
if (pattern.findall(input_word)):
    print('The word must contain only letters not numbers, spaces or characters')

# convert all to lowercase letters

lowercase_word = input_word.lower() # taking the input_word changing this to lower case and then putting it into the lowercase_ word

# Reverse the input 

reverse_word = lowercase_word[::-1] # Reversing the characters of the word in the string lowercase_word

# Test to see if input equals reverse of input 

if (lowercase_word == reverse_word): # comparing whats in the lowercase_word contanier and the reverse_word contanier to see if its a palindreaome
    print("This word is a pallindrome")
else: 
    print("This word is not a pallindrome")



