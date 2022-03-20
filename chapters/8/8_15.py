# Python Crash Course
# Exercises 8-15 - Main Execution
# 03/10/2022
# Andrew Tracey

# Put the functions for the example printing_models.py in a separate file
# called printing_functions.py. Write an import statement at the top of 
# printing_models.py (this file) and modify the file to use the imported stuff

import printing_functions as pf


# Start with some designs that need to be 3-D printed
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Call the functions from printing_functions.py to print and show completed
pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)
