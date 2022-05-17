# Python Crash Course
# Exercises 11-1 & 11-2
# March 24, 2022

# 11-1 City, Country
# 11-2 Population
# Modify your function so it requires a third parameter, population.
# Change the parameter to be optional.

def get_formatted_city(city, country, pop=None):
	"""Return the correctly formatted City, Country reference as a string"""
	if pop:
		return f"{city.title()}, {country.title()} - population {pop:,}"
	else:
		return f"{city.title()}, {country.title()}"
