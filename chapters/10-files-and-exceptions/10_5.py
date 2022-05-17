# Python Crash Course
# Exercises 10-5
# 03/18/2022
# Andrew Tracey

# Write a while loop that asks people why they like programming.
# Each time someone enters a reason, add their reason to a file that stores
#  all the responses

filename = 'programming.txt'

while True:
	resp = input("Input one reason that you love programming ('q' to quit)? ")
	if resp.lower() == 'q':
		break
	else:
		with open(filename, 'a') as myfile:
			myfile.write(resp + '\n')
