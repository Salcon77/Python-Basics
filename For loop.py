"""
The for loop in Python is used to iterate over a sequence (list, tuple, string) or other iterable objects.
Iterating over a sequence is called traversal.
"""

# Program to find the sum of all numbers stored in a list

# List of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# variable to store the sum
sum = 0

# iterate over the list
for val in numbers:
	sum = sum+val

# Output: The sum is 48
print("The sum is", sum)


# Program to iterate through a list using indexing

genre = ['pop', 'rock', 'jazz']

# iterate over the list using index
for i in range(len(genre)):
	print("I like", genre[i])

digits = [0, 1, 5]

"""
A for loop can have an optional else block as well. The else part is executed if the items in the sequence used in 
for loop exhausts.
"""
for i in digits:
    print(i)
else:
    print("No items left.")