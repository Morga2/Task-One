# Email Address Validator By Morgan Wells 

# Input: Email address as a string
# Output: 
#  1) Is the email address valid? if so a message needs to be returned to user!
#  2) The reason why the password is not valid
#  3) Suggestions for correcting the problem 

# References: 
#   Regular expression to match exact number of characters?, (n.d.) Available At: https://stackoverflow.com/questions/14590008/regular-expression-to-match-exact-number-of-characters Accessed: 30-3-19
#   Count the number of occurrences of a character in a string in Javascript, (n.d.) Available At: https://stackoverflow.com/questions/881085/count-the-number-of-occurrences-of-a-character-in-a-string-in-javascript Accessed: 30-3-19
#   Setting a minimum/maximum character count for any character using a regular expression, (n.d.) Available At: https://stackoverflow.com/questions/10518979/setting-a-minimum-maximum-character-count-for-any-character-using-a-regular-expr Accessed: 30-3-19
#   Regular expression find if same character repeats 3 or more no of times in Java, (n.d.) Available At: https://stackoverflow.com/questions/47806343/regular-expression-find-if-same-character-repeats-3-or-more-no-of-times-in-java Accessed: 30-3-19
#   Regex match A-Z, a-z, 0-9, (n.d.) Available At: https://stackoverflow.com/questions/1721602/regex-match-a-z-a-z-0-9-and Accessed: 30-3-19
#   Learn, Build, & Test RegEx, (n.d.) Available At: https://regexr.com/ Accessed: 30-3-19
#   How To Check For [a-z] In String?, (n.d.) Available At: https://bytes.com/topic/python/answers/23336-how-check-z-string Accessed: 30-3-19 
#   Isupper(), islower(), lower(), upper() in Python and their applications, (n.d.) Available At: https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/ Accessed: 30-3-19
#   Python String | split(), (n.d.) Available At: https://www.geeksforgeeks.org/python-string-split/ Accessed: 30-3-19
#   How to check a string for specific characters?, (n.d.) Available At: https://stackoverflow.com/questions/5188792/how-to-check-a-string-for-specific-characters Accessed: 30-3-19
#   Python Equality Check Difference, (n.d.) Available At: https://stackoverflow.com/questions/23220141/python-equality-check-difference/23220264 Accessed: 30-3-19

# Data Tests:
#            Good Email Address:
#               bob@gmail.com (because it meets all of the required criteria)     
#            Bad Email Address:
#               bob@gamil.com.au.il.ko (it has more than 3 dots)
#               bob a b@gmail.com (It has white space between letters)
#               bob?@Gamil.com (it has an unknown special character)
#               bob.com.au (doesn't have an @ sign)
#               bob@gmail.com..au (Has a double dot)
#               bob@gmaildotcom (does not have any dots)

# First I Imported Modules that i would need to use when solving the problem:

import re # I imported a regular expression package to help me find strings or sets of strings

# Next I set the variables:

FullEmail = "" # "" tell the computer the variable FullEmail (container) is a datatype called string and set it to empty. 
is_valid = True # is_valid, is an variable used to capture if a condition is met, either by True or False
errors = [] # errors is a List datatype to store all the errors we find 
username = "" # username is a variable that captures the first part of the email address and is a string datatype
hostname = "" # Example of a string

# Here i added the input, which was the getting the email address from user: 

FullEmail = input("Enter Email Address: ")
# FullEmail is the string, input() is the function that will store the email you enter

# Then I created a test to make sure the @ symbol that only separates username and hostname, and make sure there is only one: 

pattern = re.compile(r'@') # re.compile is a command from the re module we imported earlier, used to create a regular expression
if (not(pattern.findall(FullEmail))): # Test if the @ symbol is in the email address
    is_valid = False # If you cant find the @ in the email then set valid flag to false (using this container to tell us when something has gone wrong)
    errors.append("Email address should have a @ symbol") #errors is the list, and using append to add something to list 
    
# I Split the email address into username and hostname: 

SplitEmail = FullEmail.split('@') # Telling the email address to split at @ sign, creates a list called split email which has two strings inside list 
# print(SplitEmail[1]), Here I printed to make sure that the program was working when testing!

# Then created a test to make sure there is no white space on both username and hostname parts:

if (SplitEmail[0].isspace()): # Is there any white space by checking the SplitEmail container for the first string in the container which is username 
    is_valid = False
    errors.append("Email Address should have no white space in username")

if (SplitEmail[1].isspace()):
   is_valid = False
   errors.append("Email Address should have no white space in hostname")

# I converted any uppercase letters to lowercase letters:

username = SplitEmail[0].lower() # turn into lower case while adding to new container
#print(username), To test the algorithm works
hostname = SplitEmail[1].lower() 
#print(hostname), To test the algorithm works

# Tested that the email address only contains letters from a-z, numbers from 0 to 9 and only the special charters [.-_]:

pattern = re.compile('[^a-z0-9._-]') # Put in the patten container we are not trying to find 
if (pattern.findall(username)): # looking into the username container to see if there is anything we dont want to find is in there
    is_valid = False  # if the brackets come out true then we have found something wrong, then we set the container is_valid to false
    errors.append("username should only include letters from a to z, numbers from 0 to 9 and special characters ._-")

pattern = re.compile('[^a-z0-9._-]')
if (pattern.findall(hostname)):
    is_valid = False 
    errors.append("hostname should include letters from a to z, numbers from 0 to 9 and special characters ._-")

#print(is_valid), To test the algorithm works

# Created a test to make sure there is at least one period in the valid domain name:

pattern = re.compile('\.')
numofperiods = len(pattern.findall(hostname)) # len counts the number of characters in the string ie. number of periods 
#print (numofperiods)

if (not(numofperiods >= 1 and numofperiods <=3)): # Checking the variable numberofperiods to see if the number of perods is between 1 and 3 
    is_valid = False # Only do this line if the email has less than 1 and more than 3 periods
    errors.append("hostname should only have one to three periods in it")

#print(is_valid), To test the algorithm works

# Cant be two periods in a row in domain name

pattern = re.compile('\.\.') # you put the \ to tell the regular expression that we wont the charcater period
if (pattern.findall(hostname)): # check the hostname to see if there is double periods
    is_valid = False
    errors.append("hostname should not have two periods in a row")

# Work out if email address is valid by testing the email address criteria

if(is_valid == True): # using is valid as a flag for something going wrong 
    print("Email Address is valid") 
else:
    print("Email Address is not valid")

# If not valid display 'invalid', then provide reasons why

if(is_valid == False):
    print("This was not valid because:")
    print(errors) # If email address inst valid, print out errors.
