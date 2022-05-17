# Python Crash Course
# Chapter 10 - Page 191
# March 18, 2022

# Practice writing to a file

filename = 'chapters/10-files-and-exceptions/programming.txt'

with open(filename, 'a') as file_object:
	file_object.write("I also love finding meaning in large datasets.\n")
	file_object.write("I love creating apps that can run in a browser.\n")
