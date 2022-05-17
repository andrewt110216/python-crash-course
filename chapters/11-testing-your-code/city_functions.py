# Python Crash Course
# Exercises 11-1
# 03/24/2022
# Andrew Tracey

# 11-1
# 11-2
# Modify your function so it requires a third parameter, population.
# Change the parameter to be optional.

def get_formatted_city(city, country, pop=None):
	"""Return the correctly formatted City, Country reference as a string"""
	if pop:
		return f"{city.title()}, {country.title()} - population {pop:,}"
	else:
		return f"{city.title()}, {country.title()}"
