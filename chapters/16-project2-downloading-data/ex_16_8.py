# Python Crash Course
# Exercise 16-8
# May 22, 2022

# Exercise 16-8 - Recent Earthquakes
# You can find data files containing information about the most recent earth-
# quakes online. Download one of these data sets and create a visualization
# of the most recent activity.

import json
import math

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Load data from json file
directory = 'chapters/16-project2-downloading-data/'
# Significant earthquakes over last 30 days, downloaded 5/22/2022
filename = 'data/eq_data_prior_30_significant_2022_05_22.geojson'
with open(directory + filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']
data_title = all_eq_data['metadata']['title']

# Extract data
mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_texts.append(eq_dict['properties']['title'])

# Map the earthquakes
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [3*m for m in mags],
        'color': mags,
        'colorscale': 'YlOrRd',
        'reversescale': False,
        'colorbar': {'title': 'Magnitude'},
    }
}]

my_layout = Layout(title=data_title)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename=directory+'global_earthquakes.html')
