# Functions

# In Python, function is a group of related statements that perform a specific task.
# Functions help break our program into smaller and modular chunks. As our program grows larger and larger,
# functions make it more organized and manageable.
# Furthermore, it avoids repetition and makes code reusable.

# Keyword def marks the start of function header.
# A function name to uniquely identify it. Function naming follows the same rules of writing identifiers in Python.
# Parameters (arguments) through which we pass values to a function. They are optional.
# A colon (:) to mark the end of function header.
# Optional documentation string (docstring) to describe what the function does.
# One or more valid python statements that make up the function body. Statements must have same indentation level.
# An optional return statement to return a value from the function.
# Example of a function

def greet(name):
    """ This function greets to the person passed in as parameter """
    print("Hi nice to meet you "+ name + " good morning")

x="sal"
greet(x)
# The first string after the function header is called the docstring and is short for documentation string.
# It is used to explain in brief, what a function does.
# We can print it out by calling it on the function with .__doc__
print(greet.__doc__)

def absoluteValue():
    """this finds the absoulute value of a given number"""
    num=input("Enter a number to find its absolute value")
    num=int(num)
    if num > 0:
        return print(num)
    else:
        return print(-num)
absoluteValue()

# SCOPE
# Scope of a variable is the portion of a program where the variable is recognized.
# Parameters and variables defined inside a function is not visible from outside. Hence, they have a local scope.
# Lifetime of a variable is the period throughout which the variable exits in the memory.
# The lifetime of variables inside a function is as long as the function executes.
# They are destroyed once we return from the function. Hence, a function does not remember the value of a variable
# from its previous calls.


def scope_func():
	x = 10
	print("Value inside function:",x)

x = 20
scope_func()
print("Value outside function:",x)