# Python Crash Course
# Exercise 15-10 - Part 2
# 04/06/2022

# 15-10
# Practice using Matplotlib and Plotly libraries
# Part 2
# Try using Plotly (instead of Matplotlib) to visualize a random walk

# Plan
#  1. Set up the random walk
#  2. Figure out how to visualize the random walk using Plotly

#import plotly.express as px
import plotly.graph_objects as go

from random_walk import RandomWalk

# Create and fill the random walk
rw = RandomWalk(10_000)
rw.fill_walk()

# Visualize

# Using Plotly Express 
#fig = px.scatter(x=rw.x_values, y=rw.y_values, title='Modeling a Random Walk')

# Using Plotly Graph Objects
colors = ['blue' for _ in range(rw.number_of_points)]
colors[0:5] = ['darkorange' for _ in range(5)]
colors[-5:-1] = ['red' for _ in range(5)]
marker = go.scatter.Marker(color=colors, size=3)

data = go.Scatter(x=rw.x_values, y=rw.y_values, mode='markers+text', marker=marker, fillcolor='white')
xaxis = {'visible': False}
yaxis = {'visible': False}
layout = go.Layout(xaxis=xaxis, yaxis=yaxis, paper_bgcolor='dimgray', plot_bgcolor='wheat')
fig = go.Figure(data=data, layout=layout)

fig.show()
