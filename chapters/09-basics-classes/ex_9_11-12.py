# Python Crash Course
# Exercises 9-11 and 9-12
# March 14, 2022

# 9-11
# Using your latest User classes (9.8), store the 3 classes in one module.
# Import the module, and make an instance of Admin and call show_privileges.

# 9-12
# Separate Admin and Privileges classes into a separate module.

import admin


j_privs = ['create new user', 'delete files', 'export files']
jimmy = admin.Admin('jimmy', 'falon', j_privs, location='hollywood', age=55)

jimmy.greet_user()
jimmy.describe_user()
jimmy.privileges.show_privileges()
