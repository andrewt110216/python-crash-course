# Python Crash Course
# Exercise 8-15
# March 10, 2022

# Printing Models
# Put the functions for the example printing_models.py in a separate file
# called printing_functions.py.
# Write an import statement at the top of this file and modify the file
# to use the imported stuff

import printing_functions as pf


# Start with some designs that need to be 3-D printed
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Call the functions from printing_functions.py to print and show completed
pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)
