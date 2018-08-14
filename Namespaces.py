# NAMESPACES
"""
Name (also called identifier) is simply a name given to objects. Everything in Python is an object.
Name is a way to access the underlying object.
For example, when we do the assignment a = 2, here 2 is an object stored in memory and a is the name we associate
it with. We can get the address (in RAM) of some object through the built-in function, id().
"""
#NAMES
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

# NAMESPACES
# namespace is a collection of names.
# In Python, you can imagine a namespace as a mapping of every name, you have defined, to corresponding objects.
# Although there are various unique namespaces defined, we may not be able to access
# all of them from every part of the program. The concept of scope comes into play.

""" Here, the variable a is in the global namespace. Variable b is in the local namespace of outer_function() 
and c is in the nested local namespace of inner_function(). When we are in inner_function(), c is local to us, b is 
nonlocal and a is global. We can read as well as assign new values to c but can only read b and c from inner_function().
If we try to assign as a value to b, a new variable b is created in the local namespace which is different
than the nonlocal b. """

def outer_function():
    a = 20

    def inner_function():
        a = 30
        print('a =', a)

    inner_function()
    print('a =', a)


a = 10
outer_function()
print('a =', a)
print("")

# Here, all reference and assignment are to the global a due to the use of keyword global. So the last change
# to global a was setting it to 30 and that,s what gets printed.
a = 10
def outer_function():
    #global a
    a = 20

    def inner_function():
        global a
        a = 30
        print('a =', a)



    inner_function()
    print('a =', a)

a = 10
# Even though a is set to 10 here because it was called as a global variable earlier it doesnt change.
# And you cant call it global a here to change it you'll get a error.
outer_function()
print('a =', a)