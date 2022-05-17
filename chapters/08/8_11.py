# Python Crash Course
# Exercises 8-11
# 03/10/2022
# Andrew Tracey

# Make a list containing a series of short text messages.

# Write a function that prints each text message and moves each message to a
# new list as it's printed. After the function, print both of your lists to
# make sure the messages were moved correctly

# Now, call the function using a copy of the list of messages and confirm
# that all lists are as expected after calling the function

def sent_messages(messages: list) -> list:
	"""Print each message from the list and move it to a new list"""
	sent_messages = []
	while messages:
		current_message = messages.pop()
		print(current_message)
		sent_messages.append(current_message)
	return sent_messages


text_messages = [
	"On my way",
	"Be there soon",
	"I'll call you back later",
	"Can't talk right now",
	"Sounds great!",
]

sent = sent_messages(text_messages[:])
print("text messages:", text_messages)
print("sent messages", sent)
