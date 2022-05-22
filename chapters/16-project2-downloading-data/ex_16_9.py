# Python Crash Course
# Exercise 16-9
# May 22, 2022

# Exercise 16-9 - World Fires
# Using the data processing work from the first part of this chapter and the
# mapping work from this section, make a map that shows which parts of the
# world are affected by fires.

import csv
import numpy as np

from plotly.graph_objs import Scattergeo
from plotly import offline

# Extract data from csv file
directory = 'chapters/16-project2-downloading-data/'
filename = 'data/fire_data_modis_world_48h_2022_05_22.csv'
with open(directory + filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get column indexes
    lat_idx = header_row.index('latitude')
    long_idx = header_row.index('longitude')
    bright_idx = header_row.index('brightness')
    conf_idx = header_row.index('confidence')

    # Get locations and brightness, filtered by confidence level
    lats, longs, brights = [], [], []
    conf_level = 80
    for row in reader:
        if float(row[conf_idx]) >= conf_level:
            lats.append(float(row[lat_idx]))
            longs.append(float(row[long_idx]))
            brights.append(float(row[bright_idx]))

# Normalize brightnesses
#avg = np.average(brights)
#std = np.std(brights)
min = min(brights)
max = max(brights)
normalized_b = [(b - min) / (max - min) for b in brights]

# Plot fire locations on map
data = [Scattergeo({
                    'lat': lats,
                    'lon': longs,
                    'marker': {
                                'size': 3,
                                'color': normalized_b,
                                'colorscale': [[0, 'rgb(254,188,0)'],
                                               [0.25, 'rgb(254,151,4)'],
                                               [1, 'rgb(233,0,0)']],
                                'colorbar': {'title': 'Brightness'},
                            }
                    })]

my_layout = {'title': f'World Fires, Last 48 Hours - Conf. Level > {conf_level}%'}
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename=directory+'world_fires.html')

