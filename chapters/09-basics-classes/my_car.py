# Python Crash Course
# my_car.py (Page 175)
# 03/14/2022
# Andrew Tracey

# Import a class from an outside module and use it.

from car import Car


my_new_car = Car ('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
