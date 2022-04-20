# Python Crash Course
# Chapter 16 (Page 334)
# 04/07/2022

import csv
import matplotlib.pyplot as plt
from datetime import datetime

# Extract data from csv file
filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	print_header = False  # Set to True to print column indexes and headers
	if print_header:
		for index, header in enumerate(header_row):
			print(index, header)

	# Get dates and high temperatures
	dates, highs = [], []
	for row in reader:
		high = int(row[5])
		date = datetime.strptime(row[2], '%Y-%m-%d')
		highs.append(high)
		dates.append(date)

# Plot the temperatures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

# Format plot
ax.set_title('Daily High Temperatures. Sitka, AK (July 2018)', fontsize=16)
ax.set_xlabel('', fontsize=14)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (F)', fontsize=14)

plt.show()
