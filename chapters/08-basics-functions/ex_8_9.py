# Python Crash Course
# Exercises 8-9
# March 10, 2022

# Messages
# Make a list containing a series of short text messages.
# Pass the list to a function that prints each text message.

def show_messages(messages: list):
	"""
	Print each message from the list.
	"""
	for message in messages:
		print(message)

text_messages = [
	"On my way",
	"Be there soon",
	"I'll call you back later",
	"Can't talk right now",
	"Sounds great!",
]

show_messages(text_messages)
