#This is a program to find the average height.

#student_heights = [180 124 165 173 189 169 146] which I used
student_heights = (input("Input the list of student heights ").split())
for n in range(0, len(student_heights)):
	student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = 0
for height in student_heights:
	total_height = total_height + height 					#or total_height += height
print("Total height of all students:", total_height)

no_of_students = 0
for student in student_heights:
	no_of_students = no_of_students + 1						#or no_of_students += 1
print("Number of students:", no_of_students)

average_height = total_height / no_of_students
print("Average height of students:", round(average_height))