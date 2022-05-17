# Python Crash Course
# Exercise 11-3
# March 24, 2022

# 11-3 Employee
# Write a class called Employee, with attributes: first name, last name, and
#  annual salary, and a method give_raise with an optional raise amount that 
#  defaults to $5,000.

class Employee():
	"""Simple representation of a company employee."""

	def __init__(self, first_name, last_name, salary):
		"""Initialze the required attributes."""
		self.first_name = first_name
		self.last_name = last_name
		self.salary = salary

	def give_raise(self, raise_amount=5000):
		"""Give the employee a raise."""
		self.salary += raise_amount
