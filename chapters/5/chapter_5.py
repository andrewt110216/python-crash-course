# Python Crash Course
# Chapter 5 Exercises

import random


print("----5-5 Alien Colors #3----")
colors = ["green", "yellow", "red"]
random_color = random.randint(0, 2)
print(random_color)
alien_color = colors[random_color]
print(f"Alien color: {alien_color}")
if alien_color == "green":
    print("You earned 5 points!")
elif alien_color == "yellow":
    print("You earned 10 points!")
elif alien_color == "red":
    print("You earned 15 points!")

print("----5-6. Stages of Life----")
age = random.randint(0, 101)
print(f"Age: {age}")
if age < 0:
    print("ERROR. Please input a valid age, greater than 0.")
elif age < 2:
    print("Baby")
elif age < 4:
    print("Toddler")
elif age < 13:
    print("Kid")
elif age < 20:
    print("Teenager")
elif age < 65:
    print("Adult")
elif age > 65:
    print("Elder")

print("----5-7 Favorite Fruit----")
fav_fruits = ["apple", "blueberry", "strawberry"]
if "banana" in fav_fruits:
    print("Wow, you really like bananas!")
if "blueberry" in fav_fruits:
    print("Wow, you really like bloobs!")
if "orange" in fav_fruits:
    print("Wow, you really like oranges!")
if "watermelon" in fav_fruits:
    print("Wow, you really like watermelon!")
if "starfruit" in fav_fruits:
    print("Wow, you really like starfruit!")

print("----5-8 Hello Admin----")
print('----5-9 No Users----')
users = ['admin', 'andrew', 'lisa', 'david', 'hannah', 'leah', 'aedan']
if users:
    for user in users:
        if user == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print(f'Hello {user.title()}, thank you for logging in again.')
else:
    print('We need to find some users!')

print('----5-10 Checking Usernames----')
current_users = ['admin', 'ANDREW', 'LISA', 'david', 'hannah', 'leah', 'Aedan']
current_users_lower = [user.lower() for user in current_users]
new_users = ['Jake', 'erica', 'STEVE', 'Kelsey', 'leah', 'AEDAN']
if new_users:
    for new in new_users:
        if new.lower() in current_users_lower:
            print(f'Sorry {new}, that username is taken. Please enter a new username.')
        else:
            print(f'{new} is an available username!')
else:
    print('We need to find some users!')

print('----5-11 Ordinal Numbers----')
nums = list(range(1, 10))
for num in nums:
    if num == 1:
        print('1st')
    elif num == 2:
        print('2nd')
    elif num == 3:
        print('3rd')
    else:
        print(f'{num}th')
