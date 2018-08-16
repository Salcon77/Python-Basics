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

# We can generate a sequence of numbers using range() function. range(10) will generate numbers
# from 0 to 9 (10 numbers).
print(range(10))
# To get this function to print all numbers between 0-10 we can use the function list()
print(list(range(10)))
# note how it starts at 0 and ends at 9 instead of starting at 1 and ending at 10

# We can use the range() function in for loops to iterate through a sequence of numbers.
# It can be combined with the len() function to iterate though a sequence using indexing.


genre = ['pop', 'rock', 'jazz']

# iterate over the list using index
# it iterates for the len() of the list genere
for i in range(len(genre)):
    print("I like", genre[i])

print("the length of the list genere is {}".format(len(genre)))

digits = [0, 1, 5]


for i in digits:
    print(i)
# Once i is done iterating through every index of the list digit the for loop ends and goes to the else block.
else:
    print("No items left.")