# NAMESPACES
"""
Name (also called identifier) is simply a name given to objects. Everything in Python is an object.
Name is a way to access the underlying object.
For example, when we do the assignment a = 2, here 2 is an object stored in memory and a is the name we associate
it with. We can get the address (in RAM) of some object through the built-in function, id().
"""

a = 2
b = 2
# Output: id(2)= 10919424
print('id(2) =', id(2))

# Output: id(a) = 10919424
print('id(a) =', id(a))

# Output: id(b) = 10919424
print('id(a) =', id(b))

def printHello():
    print("Hello")
a = printHello()

# Output: Hello
a