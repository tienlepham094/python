class Employee:
	raise_amnt = 1.04
	def __init__(self, name, pay):
		self.name = name
		self.pay = pay

# inheritance
class Developer(Employee):
	raise_amnt = 1
	def __init__(self, name, pay, pro_lang):
		# super from parent
		super().__init__(name,pay)
		# Employee.__init__(self, name, pay)
		self.pro_lang = pro_lang


class Manager (Employee):
	def __init__(self, name,pay, employees = None):
		super().__init__(name, pay)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees


	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)


	def show_emp(self):
		if len(self.employees) > 0:
			for index,emp in enumerate(self.employees):
				print("Employee "+ str(index+1)+ " : "+ emp.name)
		else:
			print("No employees")

dev_1 = Developer("John", 20000, "Python")
dev_2 = Developer("Kelly", 10000, "Java")

mng = Manager("Sam", 50000, [dev_1])
mng.show_emp()

print("------------------------------")
# add employee
mng.add_emp(dev_2)
mng.show_emp()