#List Methods

#l.append() - this will add the element written in this at the last of the list

l = [1, 2, 4, 5, 7, 9]

l.append(7)			# works for numbers and strings both
print(l)

#l.sort() - this will sort the elements

l.sort()
print(l)

l.sort(reverse=True) 	#reverse for reverse order and True is case-sensitive. 
print(l)

#l.reverse() - to reverse the order of elements

l.reverse()
print(l)