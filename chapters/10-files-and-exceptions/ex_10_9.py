# Python Crash Course
# Exercise 10-9
# March 21, 2022

# Silent Cats and Dogs
# Modify your code from 10-8 to fail silently if a file is not found.

def print_names(file_name):
	"""Print the names found in a text file."""
	try:
		with open(file_name, encoding='utf-8') as f:
			contents = f.read()
	except FileNotFoundError:
		pass
	else:
		names = contents.split()
		print(f"The following names were found in {file_name}:")
		for name in names:
			print(f" - {name.title()}")

directory = 'chapters/10-files-and-exceptions/'
filenames = ['cats.txt', 'fish.txt', 'dogs.txt']
for filename in filenames:
	print_names(directory + filename)
