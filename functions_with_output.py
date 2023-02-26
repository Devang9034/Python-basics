def format_name(f_name, l_name):
	#Docstring
	"""Take the first and last name and format it to return the title case version of the name."""
	if f_name == "" or l_name == "":
		return "You didn't provide any inputs."
	formated_f_name = f_name.title()
	formated_l_name = l_name.title()
	return f"{formated_f_name} {formated_l_name}"

print(format_name(input("Enter your first name:"), input("Enter your last name:")))
