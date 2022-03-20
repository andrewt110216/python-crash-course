# Python Crash Course
# Chapter 3 Exercises
# 

# 3.4-7 Dinner Guest List

# 3.4
# Guests I would like to invite to dinner
guests = ["Barack Obama", "Rachel Bilson", "Neil Patrick Harris", "Javy Baez", "Kendrick Lamar"]

# 3.5
# Javy can't attend
print(f"A guest has informed that they cannot attend the dinner. He sends his regrets")
absent = "Javy Baez"

# Replace absent guest
i = guests.index(absent)
print(i)
guests.remove(absent)
guests.insert(i, "Ryan Theriot")

# 3.6
# Found a bigger table
print('Dearest Guests,\n\n\tA larger table has opened up. '
	  'Invitations will be extended to 3 additional guests.\n')

# Add guests at beginning, middle, and end
guests.insert(0, "Pitbull")
guests.insert(len(guests)//2, "Michelle Obama")
guests.append("David Spade")

# 3.7
# Shrinking guest list
print('Guests,\n\n\tWe regret to inform our guests that our table will not arrive '
	  'on time. We must now reduce our guest list to just 2 guests.\n')

for _ in range(len(guests)-2):
	removed = guests.pop()
	print(f"Dear {removed}: I regret to inform you that you've been "
		"cut from the guest list to our dinner. Tough Break.\n")

# Send out new invites to current guests
for guest in guests:
	print(f"Dear {guest},\n\n\t You are hereby cordially invited to "
		"join me for dinner on the evening of September 24th."
		"\n\nSincerely,\nAndrew\n")

# Clear the list using del
del guests[1]
del guests[0]
print(guests)