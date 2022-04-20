# Python Crash Course
# Chapter 15 (Pages 316-318)
# 04/04/2022

"""Set of classes to model a random walk"""

from random import choice


class RandomWalk():
	"""A representation of a random walk on an x-y plot"""

	def __init__(self, number_of_points=5_000):
		"""Set up the initial attributes of the random walk"""
		self.number_of_points = number_of_points

		# All random walks will begin at (0, 0)
		self.x_values = [0]
		self.y_values = [0]

	# 15-3: Refactor fill_walk by creating a new method called get_step()
	def _get_step(self):
		"""Generate a step to increment the x or y value for the next point"""
		direction = choice([-1, 1])
		magnitude = choice([0, 1, 2, 3, 4])
		step = direction * magnitude
		return step

	def fill_walk(self):
		"""Generate the x and y values for each step of the random walk"""

		while len(self.x_values) < self.number_of_points:

			# Get incremental steps for new point
			x_step = self._get_step()
			y_step = self._get_step()

			# Ignore point if steps does not move
			if x_step == 0 and y_step == 0:
				continue

			# Generate new x and y values
			x_value = self.x_values[-1] + x_step
			y_value = self.y_values[-1] + y_step

			# Add new values to random walk
			self.x_values.append(x_value)
			self.y_values.append(y_value)

if __name__ == '__main__':
	# Demonstrate the results of an instance of RandomWalk
	steps = input('Enter the number of steps for the random walk: ')
	try:
		steps = int(steps.strip())
	except:
		print("The number of steps must be an integer. Try again.")
	else:
		rw = RandomWalk(steps)
		rw.fill_walk()
		print("---x_values:")
		print(rw.x_values)
		print("---y_values:")
		print(rw.y_values)
