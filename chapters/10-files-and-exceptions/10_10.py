# Python Crash Course
# Exercises 10-10
# 03/21/2022
# Andrew Tracey

# Download a few texts from Project Gutenburg that you would like to analyze.
# Write a program to count the number of times "the" is found.
# Try counting the number of times "the " is found instead, to exclude cases
#  of "then" or "there"

def word_counter(file_name, word):
	"""Count the number of times a word occurs in a file."""
	try:
		with open(file_name, encoding='utf-8') as f:
			contents = f.read()
	except FileNotFoundError:
		print(f"Sorry, the file {file_name} could not be found.")
	else:
		count = contents.count(word)
		print(f"The word '{word}' was found {count:,} times in {file_name}.")

filenames = ['tale_of_two_cities.txt', 'odyssey.txt', 'scarlet_letter.txt']
for filename in filenames:
	word_counter(filename, "the")
	word_counter(filename, "the ")
	word_counter(filename, " the ")
