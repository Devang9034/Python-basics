#The number which is totally divisible by 3 and 5 will print Fizz and Buzz and the number which is totally divisible by both will print FizzBuzz

for number in range(0, 101):
	if number % 3 == 0 and number % 5 == 0:
		print("FizzBuzz")
	
	elif number % 3 == 0:
		print("Fizz")

	elif number % 5 == 0:
		print("Buzz")

	else:
		print(number)