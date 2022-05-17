# Python Crash Course
# Exercises 6-1 through 6-10
# December 26, 2021

print('----6-1 Person----')
lisa = {
    'first name': 'Lisa',
    'last name': 'Cappuccino',
    'birthday': 'September 27, 1992',
    'city': 'Chicago',
    'college': 'Depaul',
    'favorite team': 'Da Bears',
    'bedtime': '9:00',
}
for key in lisa:
    print(f"Lisa\'s {key} is {lisa[key]}")

print('----6-3 Glossary----')
glossary = {
    'dictionary': 'A mutable unordered collection of key:value pairs.',
    'list': 'A mutable ordered collection of objects.',
    'index': 'An integer that refers to the position of an element in an '
             'ordered collection.',
    'string': 'An immutable ordered collection of letters, numbers, or '
              'characters.',
    'for loop': 'A python structure that repeats a set of commands for each '
                'item in an iterable collection.',
    'tuple': 'An immutable ordered collection of objects.',
    'modulo (%)': 'A mathematical operator that returns the remainder from '
                  'dividing the numerator by the denominator.',
    'set': 'An unordered collection of unique objects. The set() function '
           'takes a list input and returns a set.',
    'sorted()': 'A built-in function that sorts the input and returns '
                'the sorted collection.',
}
for word in glossary:
    print(f'{word.upper()}:\n    {glossary[word]}\n')

print('----6-5 Rivers----')
rivers = {'nile': 'egypt', 'amazon': 'brazil', 'mississippi': 'united states '
                                                              'of america',
          'yangtze': 'china'}
for river, country in rivers.items():
    print(f'The {river.title()} is a major river located in {country.title()}.')

for river in rivers:
    print(river.title())

for country in rivers.values():
    print(country.title())

print('\n----6-7 People----')
ben = {
    'first name': 'Benjamin',
    'last name': 'Coldbrew',
    'birthday': 'December 7, 1996',
    'city': 'Chicago',
    'college': 'Northwestern',
    'favorite team': "Cam Newton's Team",
    'bedtime': '11:00',
}
andrew = {
    'first name': 'Andrew',
    'last name': 'Drip',
    'birthday': 'January 14, 1992',
    'city': 'Chicago',
    'college': 'Northwestern',
    'favorite team': "Chicago Cubs",
    'bedtime': '10:00',
}
people = [lisa, ben, andrew]
for person in people:
    print(f"--Next Person: {person['first name']}---")
    for key in person:
        if key != 'first name':
            print(f"{person['first name']}'s {key} is {person[key]}")

print('\n----6-8 Pets----')
pets = [
    {
        'name': 'Stinson',
        'owner': 'Lisa',
        'pet type': 'cat',
        'weight (lbs)': 13,
        'rating (1-5)': 2,
        'breed': 'siberian'
    },
    {
        'name': 'Lily',
        'owner': 'Andrew',
        'pet type': 'cat',
        'weight (lbs)': 8,
        'rating (1-5)': 5,
        'breed': 'domestic short-hair'
    },
    {
        'name': 'Doug',
        'owner': 'Andrew',
        'pet type': 'fish',
        'weight (lbs)': 0.5,
        'rating (1-5)': 4,
        'breed': 'gold'
    }
]

for pet in pets:
    print(f"\n--Next Pet: {pet['name']}--")
    print(f"\t{pet['name']} is a {pet['breed']} {pet['pet type']} that "
          f"weighs {pet['weight (lbs)']} pounds, owned by {pet['owner']}.")

print('\n----6-9 Favorite Places----')
favorite_places = {
    'lisa': 'France',
    'andrew': 'Ireland',
    'dad': 'Outer Banks',
    'mom': 'Maine',
    'ronnie': 'Bratislava',
    'tj': 'St. Andrews'
}

for person in favorite_places:
    print(f"{person.title()}'s favorite place is {favorite_places[person]}")

print('\n----6-10 Cities----')
cities = {
    'Chicago': {
        'Country': 'USA',
        'Population': 2710000,
        'Fact': 'Freezing',
    },
    'Los Angeles': {
        'Country': 'USA',
        'Population': 3967000,
        'Fact': 'Sunny',
    },
    'Dingle': {
        'Country': 'Ireland',
        'Population': 2050,
        'Fact': 'Fishing Town',
    }
}

for city in cities:
    print(f"\n{city}:")
    print(f"\tCountry: {cities[city]['Country']}")
    print(f"\tPopulation: {cities[city]['Population']:,}")
    print(f"\tFact: {cities[city]['Fact']}")
