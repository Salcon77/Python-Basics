import random

# Print a random int between 10 and 20
print(random.randrange(10,20))

x = ['a', 'b', 'c', 'd', 'e']

# Print arandom element form the list x
print(random.choice(x))

# Shuffle the elements in list x
random.shuffle(x)

# Print to show the shuffled elements
print(x)

# Print a random element
print(random.random())