# Python Crash Course
# Exercises 10-10
# March 21, 2022

# Common Words
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

directory = 'chapters/10-files-and-exceptions/'
filenames = ['tale_of_two_cities.txt', 'odyssey.txt', 'scarlet_letter.txt']
for filename in filenames:
	word_counter(directory + filename, "the")
	word_counter(directory + filename, "the ")
	word_counter(directory + filename, " the ")
