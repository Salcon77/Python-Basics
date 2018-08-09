# In Python you can convert between different data types by using different
# type conversion functions like int(), float(), str() etc.

# In the example below the float function takes the int and converts its to a float
print(float(5))

# Conversion from float to int will truncate the value (make it closer to zero).
print("converting float 5.5 to a int returns ", int(5.5))
print("converting float 4.4.5 to a int returns ", int(4.4))
print("converting float 7.8 to a int returns ", int(7.8))

# Conversion to and from string must contain compatible values.
# you can not convert a letter to a float or int
# below you can  see various ways strings can be converted into floats and ints
print("converting the the string '1.5' to the float", float("1.5"))
print("converting the the string '2' to the int", int('2'))
print("converting the the string '1.5' to the int", int(1.5))
print("converting the the string '3' to the float", float('3'))
print("converting the the string '3j' to the complex", complex('3j'))

# you can convert data sets into other types of data sets
# notice how the set tuple and list are functions and you need to pass a argument in the()

x = [ 1, 2, 3, 4]
print("this is the list x", x)
print("this is converting the list x into a set", set(x))
print("this is converting the set x into a tuple",tuple(x))
print("this is converting the tuple x back into a list",list(x))


# you can convert a string into a list with each letter as a its own index
print("this is turning the string 'hello' into a list", list("hello"))



