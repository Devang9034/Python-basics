#For if else statements
#This is a python automatic pizza program

print("Welcome to Python Pizza Delieveries!")
size = input("What size pizza do you want? S, M, or L \n")
add_pepperoni = input("Do you want Pepperoni? Y or N \n")
extra_cheese = input("Do you want extra cheese? Y or N \n")

if size == "S":
	bill = 15
	print("You have choosen small size")
	
	if add_pepperoni == "Y":
		bill += 2
		print("You want Pepperoni")

	elif add_pepperoni == "N":
		print("You don't want Pepperoni")

	else:
		print("Invalid Input")


elif size == "M":
	bill = 20
	print("You have choosen medium size")

	if add_pepperoni == "Y":
		bill += 3
		print("You want Pepperoni")

	elif add_pepperoni == "N":
		print("You don't want Pepperoni")

	else:
		print("Invalid Input")

elif size == "L":
	bill = 25
	print("You have choosen large size")

	if add_pepperoni == "Y":
		bill += 3
		print("You want Pepperoni")

	elif add_pepperoni == "N":
		print("You don't want Pepperoni")

	else:
		print("Invalid Input")

else:
	print("Invalid Answer")

if extra_cheese == "Y":
	bill += 1
	print("You ordered extra cheese in your order")

print(f"Your Bill is: ${bill}")
