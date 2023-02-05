#This contains break and continue statements of python
#Break will skip the loop and continue will skip the iteration



for i in range(12):
	if(i==10):					#Continue Example
		continue
	print("5 X", i+1, "=", 5 * (i+1))

i = 0
while True:					#Break Example
	print(i)
	i = i + 1
	if(i%20 == 0):
		break