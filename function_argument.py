# There are 4 types of arguments that we can provide in a function:

# Default Arguments - We can provide a default value while creating a function.
# Keyword Arguments - We can provide arguments with key = value, this way regonizes the arguments by parameter name.
# Variable Length Arguments-
# Required Arguments 

#Examples:
#Default Argument

def average(a=5, b=5):								#a and b are declared in the function and whenever the function is called, it will give output according to the value of these varibles, but when the function is called and other value is given in that function, it will ignore the values used before.
	print("The average of a and b is", (a+b)/2)

average(1, 5)										#here the predefined value is ignored and new values are taken

#Keyword Argument

def average(a=5, b=5):								
	print("The average of a and b is", (a+b)/2)

average(b=1, a=5)									#here the a and b are used as keys, and no specific order is required for it ie (a=value, b=value or b=value, a=value) but it is necessary to pass correct arguments.

#Variable Length Argument



