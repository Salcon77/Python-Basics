"""
Decision making is required when we want to execute a code only if a certain condition is satisfied.

The if…elif…else statement is used in Python for decision making.
"""

# If the number is positive, we print an appropriate message

num = 3
if num > 0:
    print(num, "is a positive number.")
print("This is always printed.")

num = -1
if num > 0:
    print(num, "is a positive number.")
print("This is also always printed.")

# Program checks if the number is positive or negative
# And displays an appropriate message

x=  input("enter a number")

x=int(x)

if x > 0:
    print("The number you entered is {} and is greater than 0".format(x))
else:
    print("The number you entered is {} and is less than 0".format(x))

# This only takes numbers if someone puts in a letter it returns a error
# If you put in 0 you get the else statement because 0 is not greater than 0


#ELIF
# The elif is short for else if. It allows us to check for multiple expressions

# In this program,
# we check if the number is positive or
# negative or zero and
# display an appropriate message

num = 3.4

y =input("Enter a number")
y=int(y)

if y > 0:
    print("The number you entered is {} and is greater than 0".format(x))
elif y == 0:
    print("The number you have entered is {}".format(y))
else:
    print("The number you entered is {} and is less than 0".format(y))


z= input("Enter a number")
z=int(z)

if z >= 0 and z <= 5:
    print ("the number you have entered is between 0 and 5")
elif z>=6 and z <=10:
    print("the number you have entered is between 6 and 10")
else:
    print("the number you have entered is greater than 10")

