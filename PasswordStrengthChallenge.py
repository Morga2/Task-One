# Test Password Strength

# Input: Password as String
# Outputs: 
#  1) Is Password Valid
#  2) What is the Password Strenth - Poor Strength, Good Strength, Excellent Strength
#  3) Message, Error and what criteria is not met, or success message
#
#  
# References: Python Standard Library https://docs.python.org/3/library/stdtypes.html#str.isdigit
#             Python for Beginners https://www.youtube.com/watch?v=rfscVS0vtbw  
#             Regular Expressions https://regexr.com/
#             Python Tutorial https://www.w3schools.com/python/default.asp
#             What makes a password strong https://www.technologyreview.com/s/542576/youve-been-misled-about-what-makes-a-good-password/
#             Problem caculating length https://www.reddit.com/r/learnprogramming/comments/2g3l40/python_len_returns_the_wrong_value_while_working/
#
#   Tests:
#       Good Password: A1#fdsadfsfd
#       Bad Password: a1#fdsadfsfd - No capitals
#       Bad Password: Aa#fdsadfsfd - No numbers
#       Bad Password: A1dfdsadfsfd - No symbols
#       Bad Password: A1#f         - Less than 8
#       Bad Password: A1?fdsadfsfd - Wrong Symbol
#       Bad password: ersw         - Lots of things wrong
#       Poor Strength: A1#fdsad
#       Good Strength: A1#fdsadfsf
#       Excellent Strength: A1#fdsadfsfd12ffws2


# Import Modules Used 

# Need Regular Expressions Module
import re

# Set Variables

password = "" # Password is a string
is_valid = True
errors = []
strength = ""

# Get the password from user

password = input("Enter a password:")

# Test password for length - greater than or equal to 8

# Note: We need to use strip to remove carridge return from end of input otherwise the length is one more than it actually is

if (len(password.strip()) < 8):
    is_valid = False
    errors.append("Password is less than 8 characters")


# Test Password - no white space

if (password.isspace()):
    is_valid = False
    errors.append("Password has Whote Space")


# Test Password - At least one upper case letter

def hasUpper(inputString):
    return any(char.isupper() for char in inputString)

if (not(hasUpper(password))):
    is_valid = False
    errors.append("Password has no capital letter")

# Test Password - Atleast one number

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

if (not(hasNumbers(password))):
    is_valid = False
    errors.append("Password has no number") 

# Test Password - At least one symbol

if ((not (re.search("[^a-zA-Z0-9\s]", password)))): # Test using Regular Expression
    is_valid = False
    errors.append("Password has no symbol") 


# Test Password - Only allowed Symbols - $ # - _ & %

if ((not (re.search("[$#\-_&%]", password)))):
    is_valid = False
    errors.append("Password has no corerct symbol - $ # - _ & $")


# Work out password strength

# Strength Rules:
#   Poor Password has only 8 length
#   Good Password has between 8-12 Length
#   Excellent Password has more than 12


if (len(password.strip()) == 8):
    strength = "poor strength"
elif(len(password.strip()) > 8 and len(password) <= 12):
    strength = "good strength"
else:
    strength = "excellent strength"   

# Is password valid? - Password passes all tests. Tell user if good or not

if(is_valid == True):
    print("Password is valid")
else:
    print("Password is not valid")


# If Valid - Tell User Password Strength

if (is_valid == True):
    print(strength)

# If Invalid - Tell them there is an error and what is wrong

if(is_valid == False):
    print(errors)

