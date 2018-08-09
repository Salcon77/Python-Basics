# A String is sequence of Unicode characters.
# We can use single quotes or double quotes to represent strings.
# Multi-line strings can be denoted using triple quotes, ''' or """
# Strings are immutable


print("yolo")

# how to create a new line in string string
# \n jumps to a new line
print("yo \nlo")

# how to display quotation marks within a string
# to display quotation marks have a \ before the "
print("\"yolo\"")

# concatenation
# + operator combines the phrase variable with the yolo string because the phrase variable is also a string data type
phrase =  "You Only Live Once"
print(phrase + " YOLO")

# access built in functions with .
# the upper function sets the entire string to upper case
print(phrase.upper())

# the .isupper fuction checks to see if the entire string is uppercase
# because its not we get false
print(phrase.isupper())

# you can use functions in combination
# because we used the upper function before the isupper function we get true
print(phrase.upper().isupper())

# the len function returns the length of a string
# notice how this function takes argument/parameter instead of being called by .
print(len(phrase))

# you can return a single letter from a string based off its index
# indexes start with 0
# You only live once
# 0123456789
# spaces also count as indexes so if you print index 3 you get a blank as shown when you run the code
print(phrase[3])
print (phrase[4])

# index function returns what index the letter is at. If the letter is not in the string you get an error. Case matters
# if you pass an entire word or phrase you'll get the starting index of it for the first occurrence
print(phrase.index("l"))
print (phrase.index("Only"))
print(phrase.index("Once"))

# replace function replaces one string with another
print(phrase.replace("You" , "I"))