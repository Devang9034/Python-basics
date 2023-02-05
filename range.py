#This is a program in which range function is used with for loop. I am going to print sum of all number between 1 to 100

total = 0
for number in range(0, 101):						#range function ignore the last value ie if I wrote 100 it'll calculate to 99 only
	total += number									#steps can also be added by range(0, 10, 3) the last element 3 is for steps		
print(f"Sum of all the numbers is: {total}")		

