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

#Nesting a List in a Dictionary

travel_log = {
	"France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
	"Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 10}
}

#Nesting dictionary in a list
travel_log = [

	{
	"country": "France",
	"cities_visited": ["Paris", "Lille", "Dijon"], 
	"total_visits": 12
	},

	{"country":"Germany", 
	"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
	"total_visits": 10}
]

#Nesting a dictionary in a dictionary
travel_log = {
	"France": {"cities_visited": ["Paris", "Hamburg", "Stuttgart"], "total_visits": 12},
	"Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 10}
}

#Nesting dictionary in a list
travel_log = [

	{
	"country": "France",
	"cities_visited": ["Paris", "Lille", "Dijon"], 
	"total_visits": 12
	},

	{"country":"Germany", 
	"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
	"total_visits": 10}
]

print(travel_log)