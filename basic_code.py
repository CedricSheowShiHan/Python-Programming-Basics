# welcome to my python programming code tutorial! 
# In this tutorial, we will cover the basics of Python programming, including variables, data types, control structures, functions, and more. Let's get started!

# Basics of Syntax rules

## case sensitivity

# declaring variable name:
name = 'cedric' # we are free to use either ' or " when declaring variable
Name  = 'Cedric' # this is a different variable from 'name' because of case sensitivity

# lets try to print out the variables: 

print (name)
print (Name)

# --------------------------------
#single line comment

print('Hello World') # Note: To include either the double or single inverted commas in a string.

# --------------------------------

# Simple addition 
a = 5
b = 10
c = a + b #simple declaration of few variables a b c etc, and do simple summation / addition 
print(c)


# --------------------------------

# Simple subtraction
x = 15
y = 20 

print (x-y)
# Answer is negative 5 (-5), as we subtract 15 from 20, which will result in a negative output.

# --------------------------------

# Multiple statements in single line 
x = 5 
y = 10
z = x + y

print (z)

print (x, y, z)

# --------------------------------

# we are also able to detect the type of which the code is in (ie: is it an integer, string, float, etc) using the type() function.
print (type(x)) # this will return the type of variable x, which is an integer (int)
print (type(name)) # this will return the type of variable name, which is a string

# Output x = class 'int', which means that variable x has been classifed as integer (int) data type, and name = class 'str', which means that variable name has been classified as string (str) data type.
# In Python, there are several built-in data types, including:
# - int: for integers (whole numbers)
# - float: for floating-point numbers (decimal numbers)
# - str: for strings (text)
# - bool: for boolean values (True or False)
# - list: for ordered collections of items
# - tuple: for ordered, immutable collections of items
# - dict: for key-value pairs (dictionaries)

variable = 10 
print (type(variable))

# the output prints <class 'int'>, which means that the variable has been classified as an integer (int) data type. In Python, the type() function is used to determine the data type of a variable or value.
variable = "Cedric"
print(type(variable))
# Now the output prints <class 'str'>, meaning it has been classified as a string (str) data type. 


