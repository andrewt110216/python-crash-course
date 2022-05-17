# Python Crash Course
# Exercises 11-1 & 11-2
# 03/24/2022
# Andrew Tracey

# 11-1
# Write a test function to test the get_formatted_city function from
#  the separate module city_functions.py

# 11-2
# Add a third required input to the function, for population.
# Rerun the test to confirm that it now fails...confirmed.
# Modify the function so the population parameter is option. Run the test
#  again to confirm that is now passes...confirmed.
# Write a second test that verifies the function call if a population is 
#  included as an optional arguement and make sure both tests now pass...yes.

import unittest
from city_functions import get_formatted_city

class CitiesTestCase(unittest.TestCase):
	"""Tests for 'city_functions.py'."""

	def test_city_country(self):
		"""Test input with a city and a country."""
		formatted_city = get_formatted_city(
			'santa monica', 'united states of america')
		self.assertEqual(
			formatted_city, 'Santa Monica, United States Of America')

	def test_city_country_population(self):
		"""Test input with a city, country, and population."""
		formatted_city = get_formatted_city(
			'santa monica', 'united states of america', 91577)
		self.assertEqual(
			formatted_city,
			'Santa Monica, United States Of America - population 91,577')

if __name__ == '__main__':
	unittest.main()
