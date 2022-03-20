# Python Crash Course
# write_message.py (Page 191)
# 3/18/2022
# Andrew Tracey

# Practice writing to a file

filename = 'programming.txt'

with open(filename, 'a') as file_object:
	file_object.write("I also love finding meaning in large datasets.\n")
	file_object.write("I love creating apps that can run in a browser.\n")
