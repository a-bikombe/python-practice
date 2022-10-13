lst = ['Jenny', 26, 'Parker', 'Parker', 10.5]
set1 = set(lst)
print(set1) # prints {10.5, 26, 'Jenny', 'Parker'}
# gets rid of duplicates

# check if value is in set
students = {'Jane', 'Carlos', 'Amy', 'Bridgette', 'Chau', 'Dmitry'}
print('Chau' in students) # returns True

# add()
students.add('George')
print('George' in students) # returns True

# .union(), .update()
students2 = {'Alice', 'Lily', 'Zhuo', 'Amy', 'Jane'}
students3 = students.union(students2)
students.update(students2)

# .remove()
students.remove('Bridgette')

for student in students:
	print(student)