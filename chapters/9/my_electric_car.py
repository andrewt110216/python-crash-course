# Python Crash Course
# my_electric_car.py (Page 176)
# 03/14/2022
# Andrew Tracey

# Import a subclass from an outside module and use it.

from car import ElectricCar


my_tesla = ElectricCar('tesla', 'model s', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
