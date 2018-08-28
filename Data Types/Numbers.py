#NUMBERS

#Python supports integers, floating point numbers and complex numbers. They are defined as int, float and
# complex class in Python.
a = 5
print(a,type(a))
b =5.0
print(b,type(b))
c = 5 + 3j
print(c,type(c+3))

#Integers and floating points are separated by the presence or absence of a decimal point. 5 is integer
# whereas 5.0 is a floating point number.
# While integers can be of any length, a floating point number is accurate only up to 15 decimal places
# (the 16th place is inaccurate).

#Complex numbers are written in the form, x + yj, where x is the real part and y is the imaginary part.

#BASE NUMBERS
# To state a binary ad the prefix 0b or 0B before the number
print(0b1101011)

# To state a octal ad the prefix 0o or 0O before the number
print(0o15)
# To state a hex ad the prefix 0x or 0X before the number
print(0xFB)

#TYPE CONVERSIONS
# In python when you ad a int with a float the end results gets converted into a float
print(1+2.0)
# You can also convert inbetween other types
print(int(2.3))
print(str(553))
print(complex('3+2j'))

# Because decimal fractions cant stored properly in binary we have to use decimals instead of floats
# Floats allow precisions up to 16 places where as decimals provide user settable precisions.
from decimal import Decimal as D
# Output: Decimal('3.3')
print(D('1.1') + D('2.2'))

# Output: Decimal('3.000')
print(D('1.2') * D('2.50'))

# Floating point operations are carried out must faster than Decimal operations.

"""
When to use Decimal instead of float?
We generally use Decimal in the following cases.

When we are making financial applications that need exact decimal representation.
When we want to control the level of precision required.
When we want to implement the notion of significant decimal places.
When we want the operations to be carried out like we did at school
"""

