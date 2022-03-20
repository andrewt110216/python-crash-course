# Python Crash Course
# my_cars.py (Page 177)
# 03/14/2022
# Andrew Tracey

# Import multiple class from an outside module and use them.

from car import Car
from electric_car import ElectricCar as EC

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = EC('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())
