#This contains functions of python
#There are two types of function: Built-in and User-defined
#Build-in Functions are pre-defined. Some examples are: min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print(), etc.


def mean(a, b):					# mean function is created to find the mean
	mean1 = (a*b)/(a+b)
	print(mean1)

def isGreater(a, b):			# isGreater function is created to find the greater number among the variables
	if(a>b):
		print("First number is larger")
	else:
		print("Second number is larger or equal")

def isLesser(a, b):				# isLesser is a function in which,suppose the programmer want to write a code after some time, so the pass keyword makes it possible to execute the code without errors. 
	pass

a = 9
b = 8
isGreater(a, b)					# isGreater function is called
mean(a, b)						# mean function is called using a and b variables

c = 8
d = 7
isGreater(c, d)					# isGreater function is called
mean(c,d)						# mean function is called using c and d variables

