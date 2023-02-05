#List is used to collect number of items in a single variable, these are changeable meaning we can alter after creation, these are seperated by square brackets.


marks = [5, 7, 9] 			#List of numbers

print(marks)


marks = [5, 7, 9, "ABC"] 			#List of numbers and strings ie strings and other data types can also be added in a list

print(marks)

#List Index
color = ["Red", "Blue", "Green", "Yellow"]
#		  [0]	  [1]	  [2]		[3]

print(color[0])
print(color[1])
print(color[2])
print(color[3])

#Negative Indexing
#First convert the negative index into positive and then it will get most understandable

print(color[len(color)-2])	#Positive 
print(color[-2])			#Negative
print(color[4-2])			#Positive

#Using if else to find the element in list.

if "Red" in color:
	print("Yes")
else:
	print("No")

#Same thing applies for strings too

if "lue" in "Blue":
	print("Yes it is present")
else:
	print("No it is not present")

#Some more indexing
color = ["Red", "Blue", "Green", "Yellow", "Pink", "Brown", "Voilet"]

print(color[:])				# (:) will make it to print all the items inside the list ie color[0:len(marks)]
print(color[1:6])			# 1st and last elements will be skipped 
print(color[1:6:2])			# it is called jump indexing, after printing an element it will print the second element after that because of 2

#List Comprehension

list = [i for i in range(4)]	# It will print the number of elements from 0
print(list)

list = [i*i for i in range(10) if i%2==0]
print(list)