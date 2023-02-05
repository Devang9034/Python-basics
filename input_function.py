#Simple function
def greet():
	print("Hello")
	print("How are you")
	print("Have a nice day")

greet()

#Input function

def greet_with_name(name):
	print(f"Hello {name}")
	print(f"How are you {name}")
	print(f"Have a nice day {name}")

greet_with_name("Jack")

#Input Function that allows more than one functions

def greet_with(name, location):
	print(f"Hello {name}")
	print(f"What is it like in {location}")

greet_with("Jack", "London")				#Positional argument

greet_with(name = "Jack", location = "London") 			#Keyword argument