# Python Crash Course
# Chapter 10 - Page 199
# March 21, 2022

# Approximate the number of words in the book Alice in Wonderland
# Text file of book contents available from Project Gutenburg online

filename = 'chapters/10-files-and-exceptions/alice.txt'
bookname = 'Alice In Wonderland'

try:
	with open(filename, 'r', encoding='utf-8') as f:
		contents = f.read()
except FileNotFoundError:
	print(f"Sorry, the file {filename} could not be found.")
else:
	start = contents.find('CHAPTER I.')
	words = contents[start:].split()
	num_words = len(words)
	print(f"There are approximately {num_words:,} in {bookname}.")
