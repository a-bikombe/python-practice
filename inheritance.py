# parent class
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def print_info(self):
		print(self.name)
		print(self.age)

# child class
class Teacher(Person):
	def __init__(self, name, age, subject):
		self.subject = subject

		Person.__init__(self, name, age)


myTeacher = Teacher("Dr. Hirani", 49, "Computer Science")
myTeacher.print_info()
print(myTeacher.subject)