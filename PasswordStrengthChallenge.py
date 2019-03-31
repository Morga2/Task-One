# Password Strength Challenge By Morgan Wells

# Input: Password as String
# Outputs: 
#  1) Is Password Valid
#  2) What is the Password Strength - Poor Strength, Good Strength, Excellent Strength
#  3) Message, Error and what criteria is not met, or success message
 
# References: Python Standard Library, (n.d.) Available At: https://docs.python.org/3/library/stdtypes.html#str.isdigit Accessed: 30-3-19
#             Python for Beginners, (n.d.) Available At: https://www.youtube.com/watch?v=rfscVS0vtbw Accessed: 30-3-19 
#             Regular Expressions, (n.d.) Available At: https://regexr.com/ Accessed: 30-3-19
#             Python Tutorial, (n.d.) Available At: https://www.w3schools.com/python/default.asp Accessed: 30-3-19
#             What makes a password strong, (n.d.) Available At: https://www.technologyreview.com/s/542576/youve-been-misled-about-what-makes-a-good-password/ Accessed: 30-3-19
#             Problem calculating length, (n.d.) Available At: https://www.reddit.com/r/learnprogramming/comments/2g3l40/python_len_returns_the_wrong_value_while_working/ Accessed: 30-3-19

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

# Input Regular Expressions (Module):
import re

# Setting Variables:

password = ""
is_valid = True
errors = []
strength = ""

# Getting password from user:

password = input("Enter a password:") 

# Note: Input is capturing the password that the user is typing and putting it into the password container

# Testing password for length greater than or equal to 8:

# Note: We need to use strip to remove carridge return from end of input otherwise the length is one more than it actually is

if (len(password.strip()) < 8):
    is_valid = False
    errors.append("Password is less than 8 characters")

# Testing that the password has no white space:

if (password.isspace()):
    is_valid = False
    errors.append("Password has White Space")

# Testing the password has at least one upper case letter:

def hasUpper(inputString):
    return any(char.isupper() for char in inputString)

if (not(hasUpper(password))):
    is_valid = False
    errors.append("Password has no capital letter")

# Testing the password has at least one number:

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

if (not(hasNumbers(password))):
    is_valid = False
    errors.append("Password has no number") 

# Testing the password has at least one symbol:

if ((not (re.search("[^a-zA-Z0-9\s]", password)))): 
    is_valid = False
    errors.append("Password has no symbol") 

# Testing the password only allowed symbols [$ # - _ & %]:

if ((not (re.search("[$#\-_&%]", password)))):
    is_valid = False
    errors.append("Password has no correct symbol - $ # - _ & $")

# Working out password strength:

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

# Is password valid?, does password pass all tests, tell the user if good or not:

if(is_valid == True):
    print("Password is valid")
else:
    print("Password is not valid")

# If valid, tell user password strength:

if (is_valid == True):
    print(strength)

# If Invalid, tell them there is an error and what is wrong:

if(is_valid == False):
    print(errors)

