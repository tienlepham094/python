"""
Method: a function associated with class

"""
# Python Object-Oriented Programming
class Employee: 
	# constructor
	# auto create when create class
	def __init__(self, first, last, pay):
		# self: the instance
		self.first = first
		self.last = last
		self.pay = pay
		self .email = first +'.' + last +'@company.com'

	def fullname(self):
		return '{} {}'.format(emp_1.first, emp_1.last)





# create object of class
emp_1 = Employee('Corney', 'Smith', 5000)
# emp_1 = Employee() => error
print(emp_1)
print(emp_1.email)

# print fullname
print('{} {}'.format(emp_1.first, emp_1.last))
print(emp_1.fullname)
print(emp_1.fullname())

Employee.fullname(emp_1) # => same ouput
emp_1.fullname() # => a instances