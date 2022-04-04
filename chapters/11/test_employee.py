# Python Crash Course
# Exercises 11-3
# 03/24/2022
# Andrew Tracey

# 11-3
# Write a test case for the Employee class.
# Use the setUp() method to create an instance of the class.
# Write tests for the give_raise() method, both with the default value,
#  and with a custom value.

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
	"""Test cases for the Employee class."""

	def setUp(self):
		"""Create an employee object for use in all tests"""
		args = ['lisa', 'grigaliunas', 96000]
		self.lisa = Employee(*args)

	def test_give_default_raise(self):
		"""Test that the default raise is working properly."""
		before_salary = self.lisa.salary
		self.lisa.give_raise()
		self.assertEqual(self.lisa.salary, before_salary + 5000)
	
	def test_give_custom_raise(self):
		"""Test that a custom raise amount is working properly."""
		before_salary = self.lisa.salary
		self.lisa.give_raise(10_000)
		self.assertEqual(self.lisa.salary, before_salary + 10_000)

if __name__ == '__main__':
	unittest.main()
