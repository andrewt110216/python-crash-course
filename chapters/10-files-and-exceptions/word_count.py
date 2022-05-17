# Python Crash Course
# Chapter 10 - Page 199
# March 21, 2022

# Count the number of words in a file

def count_words(filename):
	"""Count the approximate number of words in a file."""
	try:
		with open(filename, encoding='utf-8') as f:
			contents = f.read()
	except FileNotFoundError:
		print(f"Sorry, the file {filename} could not be found.")
	else:
		words = contents.split()
		num_words = len(words)
		print(f"There are approximately {num_words:,} in {filename}.")

directory = 'chapters/10-files-and-exceptions/'
filenames = [
	'alice.txt',
	'siddhartha.txt',
	'moby_dick.txt',
	'little_women.txt'
	]
	
for filename in filenames:
	count_words(directory + filename)
