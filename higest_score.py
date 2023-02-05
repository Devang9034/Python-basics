#student_score = 78 65 89 86 55 91 64 89 				The score that I am using

student_score = input("Input a list of students score:").split()

for n in range(0, len(student_score)):
	student_score[n] = int(student_score[n])
print(student_score)

higest_score = 0
for score in student_score:
	if score > higest_score:				#This if will compare every value of the list and store the largest value in the higest score.
		higest_score = score

print(f"Higest score is: {higest_score}")