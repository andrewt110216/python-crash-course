# Python Crash Course
# Excercises 3-4 through 3-7
# October 23, 2021

# 3-4 Dinner Guest List
# If you could invite anyone, living or deceased, to dinner, who would you invite?
# Make a list that includes at least three people you'd like to invite to dinner.
# Then, use your list to print a message to each person, inviting them to dinner.

guests = ["Barack Obama", "Rachel Bilson", "Neil Patrick Harris", "Javy Baez", "Kendrick Lamar"]

def send_invites(guests):
	print('Sending out invites'.center(80, '='))
	for guest in guests:
		print(f"\nDear {guest},\n\n\t You are hereby cordially invited to "
			"join me for dinner on the evening of September 24th."
			"\n\nSincerely,\nAndrew\n")
		print('-' * 40)
	print('All invites have been sent'.center(80, '='))

send_invites(guests)

# 3-5 Changing the Guest List
# You just heard that one of your guests can't make the dinner, so you need to send out
# a new set of invitations. You'll have to think of someone else to invite.
# 1. Starting with the program from 3-4, add a print() call at the end of your program stating
#    the name of the guest who can't make it.
# 2. Modify your list, replacing the name of the guest who can't make it with the name of the
#    new person you are inviting
# 3. Print a second set of invitation messages, for the updated guest list.

absent = "Javy Baez"
print(f"\n{absent.title()} has informed that they cannot attend the dinner. He sends his regrets.\n")
i = guests.index(absent)
guests[i] = "Anthony Rizzo"
send_invites(guests)

# 3-6 More Guests
# You just found a bigger dinner table, so more space is available.

# Inform the guests that we found a bigger table.
print('\nDearest Guests,\n\n\tA larger table has opened up. '
	  'Invitations will be extended to 3 additional guests.\n')
print('-' * 80)

# Use insert and append to add guests at beginning, middle, and end of the guest list
guests.insert(0, "Pitbull")
guests.insert(len(guests)//2, "Michelle Obama")
guests.append("David Spade")

# 3-7 Shrinking Guest List
# You just found out that your new dinner table won't arrive in time for thie dinner, and
# you only have space for two guests.

# Print a message informing guests
print('\nGuests,\n\n\tWe regret to inform our guests that our table will not arrive '
	  'on time. We must now reduce our guest list to just 2 guests.\n')

# Use pop() to remove guests from your list until there are only two remaining. Print a
# message to that personl letting them know they are no longer invited
for _ in range(len(guests)-2):
	print('-'*80, '\n')
	removed = guests.pop()
	print(f"Dear {removed}, I regret to inform you that you've been cut from the guest list to our dinner. Tough Break.\n")

# print a message to each of the two remaining people, letting them know they're still invited
for guest in guests:
	print('-'*80, '\n')
	print(f"Dear {guest}, I am delighted to inform you that you have made the short list for dinner with me. See you soon.\n")

# Use del to remove the last two names from your list, so that the list is empty. Print it to make sure it is empty
del guests[1]
del guests[0]
print('-'*80)
print('\nChecking to make sure the guest list is now empty...')
print('Guest List:', guests)
