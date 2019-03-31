# Caesar Cipher By Morgan Wells

# Input:  1) Entering text to code
#         2) Going from from plain text to cipher [Y] or cipher to plain text [N]
# Output: 1) [Y]: Cipher code
#         2) [N]: Plain text

# References:

# Reverse a string in Python, (n.d.) Available At: https://stackoverflow.com/questions/931092/reverse-a-string-in-python Accessed: 30-3-19
# Is there a "not equal" operator in Python?, (n.d.) Available At: https://stackoverflow.com/questions/11060506/is-there-a-not-equal-operator-in-python Accessed: 30-3-19
# User Input to Choose from Dictionary, (n.d.) Available At: https://python-forum.io/Thread-User-Input-to-Choose-from-Dictionary Accessed: 30-3-19  
# How to let the user select an input from a finite list?, (n.d.) Available At: https://stackoverflow.com/questions/37565793/how-to-let-the-user-select-an-input-from-a-finite-list/37567304 Accessed: 30-3-19
# How to use list as source of selection for user input?, (n.d.) Available At: https://stackoverflow.com/questions/28425204/python-how-to-use-list-as-source-of-selection-for-user-input Accessed: 30-3-19
# Get key by value in dictionary, (n.d.) Available At: https://stackoverflow.com/questions/8023306/get-key-by-value-in-dictionary Accessed: 30-3-19
# Python Conditions, (n.d.) Available At: https://www.w3schools.com/python/python_conditions.asp Accessed: 30-3-19
# Iterating each character in a string using Python, (n.d.) Available At: https://stackoverflow.com/questions/538346/iterating-each-character-in-a-string-using-python Accessed: 30-3-19
# Is there a 'foreach' function in Python 3?, (n.d.) Available At: https://stackoverflow.com/questions/18294534/is-there-a-foreach-function-in-python-3 Accessed: 30-3-19
# Python Hash Table Implementation - Code Review Stack Exchange, (n.d.) Available At: https://codereview.stackexchange.com/questions/118110/python-hash-table-implementation Accessed: 30-3-19
# How do Python dictionary hash lookups work?, (n.d.) Available At: https://stackoverflow.com/questions/6605279/how-do-python-dictionary-hash-lookups-work Accessed: 30-3-19
# Python variables as keys to dict, (n.d.) Available At: https://stackoverflow.com/questions/3972872/python-variables-as-keys-to-dict Accessed: 30-3-19

# Data Tests:

# Good Tests: 
# (cipher to plain text)
#   hello world         
#   HELLO WORLD
# (plain text to cipher)
#   khoor zruog
#   KHOOR ZRUOG

# Cipher Tables:

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

# Seting Variables:

cipherchar = ""
inputstring = ""
result = ""
char = ""

# Defining Functions:

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

# Capturing the input string:

inputstring = input('Enter text to code: ')
direction = input('Are you going from plain text to cipher [Y] or cipher to plain text [N] : ')

# looping through each character in the input string:

for char in inputstring:
    if (direction == 'Y'):
        result = processcipher(char)
    else:
        result = reverseprocesscipher(char)
    cipherchar = cipherchar + result 
    
# Printing out cipher string:

print(cipherchar)
