#Operator OverLoading

"""
Python operators work for built-in classes. But same operator behaves differently with different types.
For example,the + operator will, perform arithmetic addition on 2 numbers, merge two lists and concatenate two strings.
"""

# Class functions that begins with double underscore _are called special functions in Python
# !!!Self note:  read more into special functions in python to get a better understanding of what they do
# https://docs.python.org/3/reference/datamodel.html#special-method-names

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # This special fuction allows us to control how the class gets printed
    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    # this special function overloads the + operator allowing us to add how we like
    # in this instance we can add one points x and y with another points corresponding x and y
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

p1 = Point(2,3)
p2 = Point(-1,2)
print(p1 + p2)
print(str(p1))