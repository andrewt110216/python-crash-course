# Python Crash Course
# Exercises 9-8
# 03/13/2022
# Andrew Tracey

# Starting with program from 9-7
# Write a separate Privileges class. The class should have one attribute
# that stores a list of strings.
# Move the show_privaleges method to this class. Make a Privelges instance
# as an attribute in the Admin class. Create a new instance of Admin and use
# the method to show its privilages

class User():
	"""Store information for individual user profile"""

	def __init__(self, first_name, last_name, **kwargs):
		self.first_name = first_name
		self.last_name = last_name
		for k, v in kwargs.items():
			setattr(self, k, v)

	def describe_user(self):
		"""Print all attributes of the user"""
		for attribute, value in vars(self).items():
			print(f"{attribute}: {value}")
		print("--------------------------")


	def greet_user(self):
		"""Greet the user with a personalized message"""
		print("--------------------------")
		print(f"Hello, {self.first_name.title()}")
		print("--------------------------")


class Admin(User):
	"""Store information for an Administrative User profile"""

	def __init__(self, first_name, last_name, privileges, **kwargs):
		"""Initialize the parent class attributes, then Admin attributes)"""
		super().__init__(first_name, last_name, **kwargs)
		self.privileges = Privileges(privileges)


class Privileges():
	"""Simple representation of a User's privileges"""

	def __init__(self, privileges):
		self.privileges = privileges

	def show_privileges(self):
		"""Display the privileges of the user"""
		print(f"The user has the following privileges:")
		for privilege in self.privileges:
			print(f"  - {privilege}")


lisa_privs = ['create user', 'remove user', "steal Andrew's food"]
lisa = Admin("lisa", "grigaliunas", lisa_privs)
print(lisa.privileges)
lisa.privileges.show_privileges()
