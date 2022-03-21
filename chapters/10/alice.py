# Python Crash Course
# alice.py (Page 199)
# 03/21/2022
# Andrew Tracey

# Approximate the number of words in the book Alice in Wonderland
# Text file of book contents available from Project Gutenburg online

filename = 'alice.txt'
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
