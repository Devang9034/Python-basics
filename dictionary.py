programming_dictionary = {
"Bug": "An error in a program that prevents the program from running as expected.", 
"Function": "A piece of code that you can easily call over and over again.",
"Loop": "The action of doing something over and over again."
}

#Retrieving items from dictionary
#print(programming_dictionary["Bug"])

#Adding new items in dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."

#print(programming_dictionary)

#Create empty dictionary 
empty_dictionary = {}

#Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

#Edit an existing dictionary
# programming_dictionary["Bug"] = "Bug is error in program"
# print(programming_dictionary)

#Loop through a dictionary 
for thing in programming_dictionary:
	print(thing)
	print(programming_dictionary[thing])