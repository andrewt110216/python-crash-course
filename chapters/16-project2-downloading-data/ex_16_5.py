# Python Crash Course
# Exercise 16-5
# May 17, 2022

# 16-5 Explore
# Generate a few more visualizations that examine any other weather aspect
# you're interested in for any locations you're curious about

# Compare the weather in Chicago vs. Santa Monica

import csv
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

class City:
    def __init__(self, name, station_ID):
        self.name = name
        self.station_ID = station_ID
        self.dates = {}
    def __repr__(self):
        return f"<class 'City': {self.name}>"
    def __str__(self):
        return self.name

# Set station ID's, all included in same CSV file
chicago = City('Chicago', 'USW00094846')
santa_monica = City('Santa Monica', 'USW00093197')
locations = [chicago, santa_monica]

# Extract data from csv file
directory = 'chapters/16-project2-downloading-data/'
filepath = 'data/chicago_santa_monica_2021-2022.csv'
with open(directory + filepath) as f:
    # Initialize reader and extract indexes from header row
    reader = csv.reader(f)
    header_row = next(reader)
    indexes_found = 0
    for index, header in enumerate(header_row):
        if header == 'STATION':
            station_index = index
            indexes_found += 1
        elif header == 'DATE':
            date_index = index
            indexes_found += 1
        elif header == 'TMAX':
            high_index = index
            indexes_found += 1
        elif header == 'TMIN':
            low_index = index
            indexes_found += 1
        elif header == 'SNWD':
            snwd_index = index
            indexes_found += 1
    if indexes_found != 5:
        raise IndexError(f'One of the required columns was not found.')

    # Extract data from csv file, row by row
    for row in reader:
        # Identify the station and corresponding city object
        station = row[station_index]
        loc = None
        for city in locations:
            if station == city.station_ID:
                loc = city

        # Skip row if station_ID was not recognized
        if loc is None:
            print(f'Station ID {station} not recognized. Entry will be skipped.')
            continue

        # Make sure date can be interpretted
        try:
            date = datetime.strptime(row[date_index], '%m/%d/%y')
        except ValueError:
            print(f"Unable to read date ({row[date_index]}) for {loc.name}.")
            quit()

        # Try to extract data points from row
        try:
            high = int(row[high_index])
            low = int(row[low_index])
            snow_depth = float(row[snwd_index] or 0)
        except ValueError:
            print(f"Missing data for {date} in {loc}. This date will be excluded.")
        else:
            loc.dates[date] = {'high': high, 'low': low, 'snow depth': snow_depth}


# Identify dates for which all locations have complete data
date_sets = [set(chicago.dates.keys()), set(santa_monica.dates.keys())]
common_dates = sorted(list(set.intersection(*date_sets)))

# Create the plot
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax2 = ax.twinx()

# Plot the data for each city, using varying colors for visual effect
colors = ['red', 'green', 'orange', 'purple', 'yellow']
max_snow_depth = 0
for index, loc in enumerate(locations):
    # Plot temperatures on primary y axis
    highs = [int(loc.dates[date]['high']) for date in common_dates]
    lows = [loc.dates[date]['low'] for date in common_dates]
    ax.plot(common_dates, highs, c=colors[index], linewidth=0.75)
    ax.plot(common_dates, lows, c=colors[index], linewidth=0.75)
    ax.fill_between(common_dates, highs, lows,
                    facecolor=colors[index],
                    alpha=0.1,
                    label=loc.name)

    # Plot snow depths on secondary y axis
    snow_depths = [loc.dates[date]['snow depth'] for date in common_dates]
    max_snow_depth = max(max_snow_depth, max(snow_depths))
    ax2.plot(common_dates, snow_depths, c=colors[index], linewidth=0.75)
    ax2.fill_between(common_dates, snow_depths, [0 for _ in snow_depths],
                    facecolor=colors[index],
                    alpha=0.25,
                    hatch='XX',
                    edgecolor=colors[index],)

# Plot 'freezing' line
ax.plot(common_dates, [32 for _ in common_dates],
        c='blue', label='Freezing', linewidth=0.75)

# Format plot
ax.set_title('Comparing Temperatures & Snow Depth (2021 and Spring 2022)',
            fontsize=16)
ax.set_xlabel('', fontsize=14)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (F)', fontsize=14)
ax2.set_ylabel('Snow Depth (Inches)', fontsize=14)
ax2.grid(False)

# Shift temperatures up
y_low, y_high = ax.get_ylim()
spread = y_high - y_low
ax.set_ylim(y_low - spread*0.25, y_high)

# Set up Snow Depth data to use the bottom 20% of the chart
y_low, y_high = ax2.get_ylim()
ax2.set_ylim(y_low, y_high*4)

# Set Snow Depth labels to the max depth, counting by 10's
upper_y_tick = round(max_snow_depth, -1) + 10
ax2.set_yticks(np.arange(0, upper_y_tick, 10))

ax.legend()
plt.savefig(directory + 'chicago_vs_santamonica_snow.png')
plt.show()
