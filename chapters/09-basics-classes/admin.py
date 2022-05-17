# Python Crash Course
# admin.py (Exercises 9-12)
# 03/14/2022
# Andrew Tracey

# Store the Admin and Privilege classes in their own separate module.

"""A set of classes to describe an administrative user of the network."""

import user


class Admin(user.User):
	"""Store information for an Administrative User profile"""

	def __init__(self, first_name, last_name, privileges, **kwargs):
		"""Initialize the parent class attributes, then Admin attributes)"""
		super().__init__(first_name, last_name, **kwargs)
		self.privileges = Privileges(privileges)


class Privileges():
	"""Simple representation of a User's privileges"""

	def __init__(self, privileges):
		self.privileges = privileges

	def __repr__(self):
		return str(self.privileges)

	def show_privileges(self):
		"""Display the privileges of the user"""
		print(f"The user has the following privileges:")
		for privilege in self.privileges:
			print(f"  - {privilege}")
