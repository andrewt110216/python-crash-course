# Python Crash Course
# Exercise 16-1
# May 16, 2022

# Sitka Rainfall
# Sitka is in a temperate rainforest, so it gets a fair amount of rainfall.
# In the data file sitka_weather_2018_simple.csv is a header called PRCP,
# which represents daily rainfall amounts. Make a visualization focusing on the
# data in this column. You can repeat this exercise for Death Valley.

import csv
import matplotlib.pyplot as plt
from datetime import datetime

directory = 'chapters/16-project2-downloading-data/data/'
filenames = ['sitka_weather_2018_simple.csv',
            'death_valley_2018_simple.csv']
data = []
for filename in filenames:
    with open(directory + filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        dates = []
        rainfalls = []
        for row in reader:
            date = datetime.strptime(row[2], '%Y-%m-%d')
            rainfall = row[3]
            if rainfall == '':
                print(f'No rainfall data for {date} in {filename}')
            else:
                rainfalls.append(float(rainfall))
                dates.append(date)
        
        data.append((dates, rainfalls))


# Create plot
plt.style.use('seaborn')
fig, ax = plt.subplots()

# Create bar charts
plt.plot(data[0][0], data[0][1], label='Sitka', c='blue', linewidth=0.8)
plt.plot(data[1][0], data[1][1], label='Death Valley', c='red', linewidth=0.8)

# Format chart
plt.xlabel('Date')
plt.ylabel('Daily Rainfall')
plt.title('Daily Rainfall - 2018 - Sitka, AK vs. Death Valley, CA')
plt.legend()

plt.tight_layout()
plt.show()