#OUTPUTS
# We use the print() function to output data
print('hello world')

# The actual syntax of the print function is print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False).
x=2
print('the variable ex is equal to', x)

# Notice how there is automatically a space between x and the string.
# to get rid of the space set sep=''and it will replace it with whatever in the quotes
print('the variable ex is equal to', x,sep='')

# If you dont want to jump to a new line after calling a print function set end='' and it will replace it with whatever
# In the quotes at the end of the print statement \n means jump to new line
# Notice how the next two statements are on the same line in console
print('the variable ex is equal to', x,sep=' ',end=' ')
print('the variable ex is equal to', x,)

# Sometimes we would like to format our output to make it look attractive.
# This can be done by using the str.format() method. This method is visible to any string object.
x = 3; y = 4
print('the value of x is {} and the value of y is {}'.format(x,y))
# {} are place holders that will be replaced by the arguments passed in the .format function

# You can also use indexes for the arguments passed in the .format function like tuple indexes
print('I love {0} and {1}'.format('bread','butter'))
print('I love {1} and {0}'.format('bread','butter'))

# You can also populate the braces with keyword and refernce them in the .format
print('That dog is {type} and his name is {name}'.format(type ="golden retriever",name = "spot"))

#INPUTS
input('Type in a number')
print("we cant do anything with what you typed in because it wasnt stored anywhere")

# This only allows you type in the console it doesnt do anything with what you typed
# To make use of what the user inputs store the input into a variable
num=input("Type in a number")
print("the number you typed in was", num)

# Notice how when you check the type of num it returns as a string <class 'str'>
print(type(num))

# If you want to do a calculation with a input you will have to convert the input into a int or float
print("If you add 3 to {} you get".format((num)), int(num)+3)

# This same operation can be performed using the eval() function.
# It can evaluate even expressions, provided the input is a string
print(eval("2+3"))

