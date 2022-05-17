# Python Crash Course
# Exercises 10-9
# 03/21/2022
# Andrew Tracey

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

filenames = ['cats.txt', 'fish.txt', 'dogs.txt']
for filename in filenames:
	print_names(filename)
