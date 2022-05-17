# Python Crash Course
# Exercise 8-11
# March 10, 2022

# Archived Messages
# Start with your work from Exercise 8-10.
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
