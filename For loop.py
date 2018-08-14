"""
The for loop in Python is used to iterate over a sequence (list, tuple, string) or other iterable objects.
Iterating over a sequence is called traversal.
"""
# Here is a list of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11, ]
# Heres a variable we will create to store the sum
sum = 0

# Here is the syntax for a for loop. We can iterate through the entire list by calling all vals in the list
# We go through every index in the list and add it to sum
# Note that in order for this to work there cant be any strings in the list
for val in numbers:
    sum=sum+val

print(sum)