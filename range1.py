#This is a program to add even numbers from 1 to 100
total = 0

for even in range(0, 101):					#Method 1
	if (even % 2 == 0):
		total += even
print(total)

# for even in range(0, 101, 2):				#Method 2
# 	total += even
# print(total)