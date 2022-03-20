# Python Crash Course
# Exercises 8-13
# 03/10/2022
# Andrew Tracey

# Start with a copy of user_profile.py from page 149.
# Build a profile of yourself by calling build_profile(), using your first and
# last names and three other key-value pairs that describe you.

import pprint


def build_profile(first, last, **user_info):
	"""Build a dictionary containing everythingwe know about a user."""
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info


user_profile = build_profile('andrew', 'tracey',
							location='santa monica',
							field='programming',
							relationship_status='married',
							age=30,
							happiness=10
							)

pp = pprint.PrettyPrinter(indent=2, sort_dicts=False)
pp.pprint(user_profile)
