"""
n Python, break and continue statements can alter the flow of a normal loop.
Loops iterate over a block of code until test expression is false, but sometimes
we wish to terminate the current iteration or even the whole loop without checking test expression.
The break and continue statements are used in these cases.
"""
# Use of break statement inside loop
# this for loops iterates over every character in the string and checks if  that character is "i" if it is
# it will break the for loop.
for val in "string":
    if val == "i":
        break
    print(val)

print("For loop over the word 'string' checking to seee 'i' and then breaking")



for val in "string":
    if val == "i":
        continue
    print(val)
print("For loop over the word 'string' checking to seee 'i' and then continuing ")