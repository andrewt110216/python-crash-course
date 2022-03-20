# Python Crash Course
# Exercises 10-1
# 03/14/2022
# Andrew Tracey

# Open a blank file in your text editor and write a few lines summarizing
#  what you've learned about Python so far. Start each line with the phrase
#  "In Python you can"... Save the file in this directory.
# Write a program that reads the file and prints what you wrote three times.
# Print the contents bonce by reading in the entire file, once by looping
#  over the file object, and once by storing the lines as a list and working
#  with them outside the with block.

filename = 'learning_python.txt'

# Method 1
with open(filename) as file_object:
	contents = file_object.read()

print(contents.strip())

# Method 2
print("------------------------------")
with open(filename) as file_object:
	for line in file_object.readlines():
		print(line.strip())


# Method 3
print("------------------------------")
with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line.strip())
