#WHILE LOOPS
# The while loop in Python is used to iterate over a block of code as long as the test expression (condition) is true.
# In while loop, test expression is checked first. The body of the loop is entered only if the
# test_expression evaluates to True. After one iteration, the test expression is checked again.
# This process continues until the test_expression evaluates to False.
n = 10
sum= 0
i= 0

while i <= n:
    sum=sum+i
    i=i+1
print("The sum of all the numbers from 1-10 is", sum)

# While loops can also have else statements that occur when the condition is false
counter = 0

while counter < 3:
    print("Inside loop")
    counter = counter + 1
else:
    print("Inside else")