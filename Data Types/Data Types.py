# Every value in Python has a data type.
# Since everything is an object in Python programming,
# data types are actually classes and variables are an instance
# (object) of these classes.

# NUMBERS
# Integers, floating point numbers and complex numbers falls under Python numbers category.
# They are defined as int, float and complex class in Python.
# 1 would be a int 1.0 would be a float and complex numbers are written in the form x+yj
# You can use the type() function to see what type a variable or value belongs to
# You can use the isinstance() function to check if a particular variable belongs to a particular class

a = 5
# returns a as a int
print(a, "is of type", type(a))

a = 2.0
# returns a as a float
print(a, "is of type", type(a))

a = 1+2j
# checks to see if a is of the complex type and returns true if it is
print(a, "is complex number?", isinstance(1+2j,complex))

# LISTS
# List is an ordered sequence of items. All the items in a list do not need to be of the same type.
# You can create a list by seperating items with commas and enclosing them in brackets []

a = [1, 2.2, 'python']
print("Everything in the a list", a) # Notice how u cant concatenate a list with a string you just separate with a comma

# remeber lists start with the index 0 so the index of 2 in the list a which would be a[2] would be the string python
print(type(a))
print ("a[2]= "+a[2])

# Lists are mutable meaning values in the list can be changed
a[1] = 3.2
print("we changed the index a[1] to 3.2 from 2.2" , a)
print(a[0:2])

# TUPLES
# Tuple is an ordered sequence of items same as list.The only difference is that tuples are immutable.
# Tuples once created cannot be modified.
# Tuples are used to write-protect data and are usually faster than list as it cannot change dynamically.
# The syntax for tuples are with parenthesis () instead of brackets and elements are separated by commas.
t = (7,'program', 3+4j)
# To reference a element in the tuples u use [] brackets but in this case its called the slicing operator
print(type(t))
print('index 1 for the tuple t is the string',t[1])

# to print a range of indexes you can use the syntax x:y to start at index x and print the next y indexes including x
print(t[0:3])

# STRINGS
# String is sequence of Unicode characters.
# We can use single quotes or double quotes to represent strings. No difference
# Multi-line strings can be denoted using triple quotes, ''' or """.
# String are immutable.
# Like list and tuple, slicing operator [ ] can be used with string
s = 'hello world'
print(type(s))
print('the index for the string variable is',s[4])
# the example below uses concatenation
print('the index for the string variable is '+s[4])

# SETS
# Set is an unordered collection of unique items.
# Set is defined by values separated by comma inside braces { }.
# Items in a set are not ordered.
a = {'1st string',5,2,3,1,"2nd string"}
print(type(a))
print("The set a = ", a)
# We can perform set operations like union, intersection on two sets. Set have unique values.
# Sets eliminate duplicates
a = {1,1,2,2,2,3,3}
print(a)

# DICTIONARIES
# Dictionary is an unordered collection of key-value pairs.
# It is generally used when we have a huge amounts of data. Dictionaries are optimized for retrieving data.
# We must know the key to retrieve the value
# In Python, dictionaries are defined within braces {} with each item being a pair in the form key:value.
# Key and value can be of any type.
d = {1:'value of 1st key', 2:'value of second key', 3:'value of 3rd key', 4:2}
print(type(d))
print(d)
# We use key to retrieve the respective value. But not the other way around.
print("the element at index 1 of the dictionary d is \"", d[1], "\"")
# The example below uses concatination notice no spaces between quotes when you run the code
print("the element at index 2 of the dictionary d is \""+ d[2]+ "\"")


