# Python Crash Course
# Chapter 15 (Page 317-322)
# 04/04/2022

"""Use Matplotlib to visualize a Random Walk on an x-y scatter plot"""

import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
	# Set up the random walk instance
	rw = RandomWalk(100_000)
	rw.fill_walk()

	# Set up pyplot plot
	plt.style.use('classic')
	fig, ax = plt.subplots(figsize=(18, 10))

	# Remove start and end points to add later for formatting purposes
	end_x = rw.x_values.pop()
	end_y = rw.y_values.pop()
	
	# Plot all points except for start and end points
	ax.scatter(rw.x_values[1:], rw.y_values[1:],
		c=range(rw.number_of_points-2), cmap=plt.cm.Blues, 
		edgecolors='none', s=1)
	
	# Plot start and end points with unique formatting
	ax.scatter(0, 0, c='green', edgecolors='none', s=40)
	ax.scatter(end_x, end_y, c='red', edgecolors='none', s=40)

	# Remove axes
	ax.get_xaxis().set_visible(False)
	ax.get_yaxis().set_visible(False)

	plt.show()

	# Allow the user to create a new random walk or exit
	keep_going = input('Make another random walk? (y/n): ')
	if keep_going.lower() == 'n':
		break
