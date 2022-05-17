# Python Crash Course
# Exercises 9-7
# 03/13/2022
# Andrew Tracey

# 9-3
# Make a class called User with attributes first name and last name, then
# create several other attributes for the user profile.
# Make a method to describe the user that prints a summary.
# Make another method t greet the user.
# Create several instances and call both methods for each.

# 9-7
# Starting with your program from 9-3, create a subclass of User for 
# administrator users. Add an attribute that stores a list of strings like:
#  "can add post", "can delete post", etc. Write a method to show the user
#  privileges and create an instance of Admin and call the method.

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
		self.privileges = privileges

	def show_privileges(self):
		"""Display the privileges of the user"""
		print(f"User {self.first_name.title()} {self.last_name.title()} has "
			"the following privileges:")
		for privilege in self.privileges:
			print(f"  - {privilege}")


lisa_privs = ['create user', 'remove user', "steal Andrew's food"]
lisa = Admin("lisa", "grigaliunas", lisa_privs)
lisa.show_privileges()
