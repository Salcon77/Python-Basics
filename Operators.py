# OPERATORS
# Operators are special symbols in Python that carry out arithmetic or logical computation

# ASTHMATIC OPERATORS
"""
+	Add two operands or unary plus	x + y

-	Subtract right operand from the left or unary minus	x - y

*	Multiply two operands	x * y

/	Divide left operand by the right one (always results into float)	x / y

%	Modulus - remainder of the division of left operand by the right	x % y (remainder of x/y)

//	Floor division - division that results into whole number adjusted to the left in the number line	x // y

**	Exponent - left operand raised to the power of right	x**y (x to the power y)

"""
x = 15
y = 4

# Output: x + y = 19
print(x,'+',y,'=',x+y, "Addition")

# Output: x - y = 11
print(x ,'-', y, '=',x-y, "Subtraction")

# Output: x * y = 60
print(x, '*', y ,'=',x*y, "Multiplication")

# Output: x / y = 3.75
print(x ,'/', y, '=',x/y,"Division")

# Output: x // y = 3
print('x // y =',x//y,"Floor Division")

# Output: x % Y = 3
print(x ,"%" , y ,'=', x % y, "Modulus remainder")

# Output: x ** y = 50625
print(x, "**", y, '=',x**y,"Exponent")
print("\n")

# COMPARISON OPERATORS
# Comparison operators are used to compare values. It either returns True or False according to the condition.
""""
>	Greater that - True if left operand is greater than the right	                        x > y
<	Less that - True if left operand is less than the right                                	x < y
==	Equal to - True if both operands are equal	                                            x == y
!=	Not equal to - True if operands are not equal	                                        x != y
>=	Greater than or equal to - True if left operand is greater than or equal to the right	x >= y
<=	Less than or equal to - True if left operand is less than or equal to the right         x <= y
"""
x = 10
y = 12

# Output: x > y is False
print('x > y  is',x>y)

# Output: x < y is True
print('x < y  is',x<y)

# Output: x == y is False
print('x == y is',x==y)

# Output: x != y is True
print('x != y is',x!=y)

# Output: x >= y is False
print('x >= y is',x>=y)

# Output: x <= y is True
print('x <= y is',x<=y)
print("\n")

# LOGICAL OPERATORS
# Logical operators are the and, or, not operators.
"""
and	True if both the operands are true	x and y
or	True if either of the operands is true	x or y
not	True if operand is false (complements the operand)	not x
"""
# Logical Operators check to see if something is true or false
x = True
y = False
print("y is ", y)
print("x is ",x)
print("using the and operator on x and y returns ", x and y, " because both have to be True in order for the and operator to be True")
print("using the or operator on x and y returns", x or y, "because only one has to be True for the or operator to be True")
# The not operator checks to see if something is False if it is it returns True.
# Because x is True the not operator returns false on it.
print("using the not operator on x returns", not x, "because the not operator checks to see if something is False")
# Because y is False the not operator returns true on it.
print("using the not operator on y returns", not y, "because the not operator checks to see if something is False")
print("\n")

# ASSIGNMENT OPERATORS
# Assignment operators are used in Python to assign values to variables.
# There are various compound operators in Python like a += 5 that adds to the variable and later assigns the same.
# It is equivalent to a = a + 5.

a = 5
print("a =", a)

# This adds 5 to a then assigns the new added number to a so a now equal 10.
a += 5
print("a += 5 equals",a)

# This subtracts 5 from a then assigns the new subtracted number to a so a now equal 5.
a -=5
print("a -= 5 equals",a)

# This multiplies a with 5 then assigns the new multiplied number to a so a now equals 25.
a *= 5
print("a *= 5 equals", a)

# This divides a by 5 and then assigns the new divided number to a so a now equals 5.
a /= 5
print("a /= 5 equals",a)

# This floor divides a by 5 then assigns the new divided number to a so a now equals 1.
a //= 5
print("a //= 5 equals",a)

# This gives the modulus remainder of a divided by 5 then assigns the new modulus remainder to as so a now equals 0.
a %= 5
print("a %= 5 equals",a, "\n")


# IDENTITY OPERATORS
# "is" and "is not" are the identity operators in Python.
# They are used to check if two values (or variables) are located on the same part of the memory.
# Two variables that are equal does not imply that they are identical.

x1 = 7
y1 = 7
x2 = "Hello"
y2 = "Hello"
x3 = [1,2,3]
y3 = [1,2,3]
print("x1 is {} y1 is {}, x2 is {}, y2 is {}, x3 is {}, y3 is {}".format(x1, y1, x2, y2, x3, y3))
print("Lets run is and is not operators on these.")

# x1 and y1 are both 7 they are equal but they are also identical because they are located in the same part of memory.
print("x1 is y1?", x1 is y1)

# Is not checks to see if they are not identical and if they are'nt it returns true as in true they are'nt identical.
print("x1 is not y1?",x1 is not y1)

# when it comes to checking strings spacing and case matters
print("x2 is y2", x2 is y2)

# Though both lists are equal in value for each index each list is mutable so each list is stored in different parts
# of memory.
print("x3 is y3", x3 is y3, "\n")

# MEMBERSIP OPERATORS
# in and not in are the membership operators in Python.
# They are used to test whether a value or variable is found in a sequence (string, list, tuple, set and dictionary).

x = 'Hello world'
print("The variable x holds the string '{}'".format(x))
y = {1:'a',2:'b'}

# Output: True
print("is the letter 'H' in x", 'H' in x)

# Case and spacing matters.
print("is the string 'hello' not in x", 'hello' not in x)

# In a dictionary we can only test for presence of key, not the value.
print("Though the letter a is in the dictionary variable y we get",'a' in y, "because you can only check for a key")
print("When we check for 1 in the dictionary variable y we ",1 in y,"because it has the key 1")





