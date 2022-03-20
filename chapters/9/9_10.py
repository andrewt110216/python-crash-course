# Python Crash Course
# Exercises 9-10
# 03/14/2022
# Andrew Tracey

# Using your latest Restaurant class (9.6), store it in a module.
# Then, import it into this file, make an instance, and call the methods.

import restaurant


roberts = restaurant.Restaurant('Roberts', 'Pizzeria')
roberts.describe_restaurant()
roberts.open_restaurant()
roberts.set_number_served(55)
roberts.increment_number_served(10)
print(f"We have now served {roberts.number_served} guests!")
