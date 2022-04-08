# instance variables: can be unique for each instance
# class variables: same each instance
class Employee:
	raise_amount = 3

	# constructor
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay

	# access class variable
	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('Corney', 'Smith', 5000)
print(emp_1.pay)


print(Employee.raise_amount)


emp_1.apply_raise()
print(emp_1.pay)