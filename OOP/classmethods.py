"""
	- A class method is a method wwhich iss belong to class
	not the object of class
	- can modify, apply across all the intances
"""
from datetime import date

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	# class method
	# can access and modify
	@classmethod
	def fromBirthDate(cls, name, year):
		return cls(name, date.today().year - year)

	# static method
	# cannot access or modify => create a static method
	@staticmethod
	def isAdult(age):
		return age > 18

person_1 = Person("John", 21)
person_2 = Person.fromBirthDate("John", 2002)

print(person_1.age)
print(person_2.age)

# print result
print(person_1.isAdult(22))
print(Person.isAdult(21))