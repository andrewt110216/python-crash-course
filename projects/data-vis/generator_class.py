# Python Crash Course
# Chapter 16 (Page 334)
# 04/07/2022

# The csv module appears to just use built-in functions for file-objects (e.g.
#  read and readlines) to turn the results into a generator instead of a list.
# From reading the Python docs at the airport on the way to Austin for Jake's
#  bachelor party, I know that it's possible to create my own generator!
# Let's give it a try.

class MyGenerator:
	"""
	A test to see if I can create a generator that works for the next function
	"""

	def __init__(self, data: list):
		self.data = data
		self._index = 0

	def __iter__(self):
		return self

	def __next__(self):
		if self._index >= len(self.data):
			raise StopIteration
		value = self.data[self._index]
		self._index += 1
		return value


mygen = MyGenerator([1, 2, 3, 4, 'apple', ('x', 'y'), 0, -12.5, ['a', 'b']])
print('index : data')
print('-' * 13)
[print(f"{i}".center(5),":",x) for i, x in enumerate(mygen)]
