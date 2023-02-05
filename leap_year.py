# This code is to find which year is the leap year 
# conditions for leap year: Every year that is evenly divisible by 4
# 							Except every year that is evenly divisible by 100
# 							Unless the year is also divisibleby 400 

year = int(input("Which year do you want to check: "))

if (year%4==0):
	
	if (year%100==0):

		if (year%400==0):
			print("It is a leap year")

		else:
			print("It is not a leap year")
	else:
		print("It is a leap year")
else:
	print("It is not a leap year")

print(year)