# Ceaser Cipher By Morgan Wells

# Input:  1) Enter text to code
#         2) Are you going from plain text to cipher [Y] or cipher to plain text [N]
# Output: 1) [Y]: Ciopher code
#         2) [N]: Plain text

# References:

# Reverse a string in Python, Available At: https://stackoverflow.com/ Acessed: 30-3-19
# Is there a "not equal" operator in Python?, Available At: https://stackoverflow.com/ Acessed: 30-3-19
# User Input to Choose from Dictionary, Available At: http://python-forum.io Acessed: 30-3-19 
# How to let the user select an input from a finite list?, Available At: https://stackoverflow.com/ Acessed: 30-3-19
# How to use list as source of selection for user input?, Available At: https://stackoverflow.com/ Acessed: 30-3-19
# Get key by value in dictionary, Available At: https://stackoverflow.com/ Acessed: 30-3-19
# Python Conditions, Available At: http://www.w3schools.com Acessed: 30-3-19
# Iterating each character in a string using Python, Available At: https://stackoverflow.com/ Acessed: 30-3-19
# Is there a 'foreach' function in Python 3?, Available At: https://stackoverflow.com/ Acessed: 30-3-19
# Python Hash Table Implementation - Code Review Stack Exchange, Available At: https://codereview.stackexchange.com/ Acessed: 30-3-19
# Algorithm - How do Python dictionary hash lookups work?, Available At: https://stackoverflow.com/ Acessed: 30-3-19
# Dictionary - Python variables as keys to dict, Available At: https://stackoverflow.com/ Acessed: 30-3-19

# Data Test

# Create the cipher tables

ciphertableupper= {
    'A': 'D',
    'B': 'E',
    'C': 'F',
    'D': 'G',
    'E': 'H',
    'F': 'I',
    'G': 'J',
    'H': 'K',
    'I': 'L',
    'J': 'M',
    'K': 'N',
    'L': 'O',
    'M': 'P',
    'N': 'Q',
    'O': 'R',
    'P': 'S',
    'Q': 'T',
    'R': 'U',
    'S': 'V',
    'T': 'W', 
    'U': 'X',
    'V': 'Y',
    'W': 'Z',
    'X': 'A',
    'Y': 'B',
    'Z': 'C'
}

ciphertablelower= {
    'a': 'd',
    'b': 'e',
    'c': 'f',
    'd': 'g',
    'e': 'h',
    'f': 'i',
    'g': 'j',
    'h': 'k',
    'i': 'l',
    'j': 'm',
    'k': 'n',
    'l': 'o',
    'm': 'p',
    'n': 'q',
    'o': 'r',
    'p': 's',
    'q': 't',
    'r': 'u',
    's': 'v',
    't': 'w',
    'u': 'x',
    'v': 'y',
    'w': 'z',
    'x': 'a',
    'y': 'b',
    'z': 'c'
}           

# Set Variable

cipherchar = ""
inputstring = ""
result = ""
char = ""

# Define Functions

def processcipher(char):

    if (char.isupper()): 
        return ciphertableupper[char]
    elif (char.islower()):
        return ciphertablelower[char]
    else:
        return char

def reverseprocesscipher(char):

    if (char.isupper()): 
        return list(ciphertableupper.keys())[list(ciphertableupper.values()).index(char)]
    elif (char.islower()):
        return list(ciphertablelower.keys())[list(ciphertablelower.values()).index(char)]
    else:
        return char

# Capture the input string

inputstring = input('Enter text to code: ')
direction = input('Are you going from plain text to cipher [Y] or cipher to plain text [N] : ')

# loop throuigh each cahrater in the input string

for char in inputstring:
    if (direction == 'Y'):
        result = processcipher(char)
    else:
        result = reverseprocesscipher(char)
    cipherchar = cipherchar + result 
    
# Print out cipher string

print(cipherchar)
