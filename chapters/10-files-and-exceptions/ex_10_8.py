# Python Crash Course
# Exercise 10-8
# March 21, 2022

# Cats and Dogs
# Create a cats.txt file and dogs.txt file, each with a few names for the
#  respective pet types. Then, write a program that opens the files and prints
#  the names. Catch the potential FileNotFoundError with a try-except loop.

# I will try to open a third non-existent file (fish.txt) to test the code.

def print_names(file_name):
	"""Print the names found in a text file."""
	try:
		with open(file_name, encoding='utf-8') as f:
			contents = f.read()
	except FileNotFoundError:
		print(f"Could not find the file {file_name}")
	else:
		names = contents.split()
		print(f"The following names were found in {file_name}:")
		for name in names:
			print(f" - {name.title()}")

directory = 'chapters/10-files-and-exceptions/'
filenames = ['cats.txt', 'fish.txt', 'dogs.txt']
for filename in filenames:
	print_names(directory + filename)
