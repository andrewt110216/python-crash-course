# Python Crash Course
# Chapter 7 Exercises
# Started: December 26, 2021
# Author: Andrew Tracey

print('----7-1 Rental Car----')
car_preferred = input("Hello. What brand rental car would you like? ")
print(f"Great! Let me see if I can find you a {car_preferred}.")

print('----7-2 Restaurant Seating----')
guests = int(input("Hello. How many guests are in your group tonight? "))
if 8 < guests <= 20:
    print("The wait will be about 15 minutes.")
elif 0 < guests < 8:
    print("Excellent, we can seat you right away.")
elif guests > 20:
    print("Sorry, we cannot seat more than 20 guests.")
elif guests <= 0:
    print("ERROR: Guests must be greater than 0.")

print('----7-3 Multiples of Ten----')
number = int(input("Please input a number and I'll tell you if it's "
                   "divisible by 10: "))
if number % 10 == 0:
    print(f"Great News! Your number {number:,} is divisible by 10.")
else:
    print(f"Unfortunately, your number {number:,} is not divisible by 10.")

print('----7-4 Pizza Toppings----')
prompt = "Please input the next topping you would like on your pizza (enter "\
         "'quit' to exit): "
topping = ""
active = True
while active:
    topping = input(prompt)
    if topping == 'quit':
        active = False
    else:
        print(f"\tWe will add {topping} to your pizza now!")

print('----7-5 Movie Tickets----')
while input != 'quit':
    age = input('Please tell me your age and I will tell you the price: ')
    if age == 'quit':
        break
    elif int(age) < 3:
        print("Your ticket is FREE!")
    elif int(age) < 13:
        print("Your ticket is $10")
    else:
        print("Your ticket is $15, you old fart")

print('----7-6 Three Exits----')
active = True
while active:
    age = input(
        'Please tell me your age and I will tell you the price ("quit" to '
        'exit): ')
    if age == 'quit':
        break
    else:
        age = int(age)
        if age < 0:
            print("ERROR: Age cannot be less than 0. Try again.")
        elif int(age) < 3:
            print("Your ticket is FREE!")
        elif int(age) < 13:
            print("Your ticket is $10")
        else:
            print("Your ticket is $15, you old fart")

print("---7-7 Infinity Loop---")
counter = 0
while True:
    print("I'm not stopping!!")
    counter += 1
    if counter == 5:
        break

# Using a while loop to remove all instances of a list
pets = ['dogs', 'cats', 'fish', 'cats', 'lizard', 'bird', 'cats']
print(pets)
while 'cats' in pets:
    pets.remove('cats')
    print(pets)

print("---7-8 Deli, 7-9 No Pastrami---")
sandwich_orders = ['Pastrami', 'Ham & Cheese', 'Turkey', 'Meatball Sub',
                   'Tuna', 'Pastrami', 'Pastrami']
finished_sandwiches = []

# Remove all Pastrami sandwich orders
print(
    "The deli is all out of Pastrami, so all orders of Pastrami will be "
    "cancelled.")
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

# Make each sandwich and move it from orders to finished.
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"Order up! One {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

# Print out each sandwich that was made.
print("The following sandwiches were made: ")
for sandwich in finished_sandwiches:
    print(f"\t{sandwich}")

print("---7-10 Dream Vacation---")
responses = {}
polling_active = True
prompt = "If you had an unlimited budget and 2 free months, what would be " \
         "your dream vacation? "

while polling_active:
    name = input('Please tell me your name: ')
    vacation = input(prompt)

    # Add to responses dictionary
    responses[name] = vacation

    # Ask if user would like to continue
    repeat = input('Would you like to let another user go? Input Y or N: ')
    if repeat == 'N':
        polling_active = False

# Print the results
for name, vacation in responses.items():
    print(f"\n\t{name}'s dream vacation is {vacation}.")
