# Python Crash Course
# Chapter 11 - Page 210-215
# March 21, 2022

def get_formatted_name(first, last, middle=None):
	"""Generate a neatly formatted full name."""
	if middle:
		full_name = f"{first} {middle} {last}"
	else:
		full_name = f"{first} {last}"
	return full_name.title()
