# Python Crash Course
# Exercises 8-1 through 8-8
# Started: December 29, 2021

print('----8-1 Message----')
def display_message():
    """Display a simple message to the user"""
    print('I am learning about Functions and Files in Python!')

display_message()

print('\n----8-2 Favorite Book----')
def favorite_book(title):
    """Display the users favorite book"""
    print(f"One of my favorite books is {title.title()}.")
favorite_book('the power of myth')

print('\n----8-3 T-Shirt (and 8-4 Large Shirts)----')
def make_shirt(size='L', message='I love Python.'):
    """Display the size and message to be printed on a t-shirt"""
    print('The t-shirt size is:', size)
    print('The message on the shirt will be:')
    print(f'\t{message}\n')

make_shirt('XXL', 'Tuck Frump!')
make_shirt('M', 'Math.')
make_shirt()

print('----8-5 Cities----')
def describe_city(name='Chicago', country='USA'):
    """Print a statement about the city"""
    print(f'{name} is in {country}.')

describe_city()
describe_city('Bratislava', 'Slovakia')

print('\n----8-7 Album (and 8-8 User Albums)----')
def make_album(artist_name, title, songs=None):
    """Return a dictionary with information about the album"""
    d = {
        'artist': artist_name,
        'title': title
    }
    if songs:
        d['songs'] = int(songs)
    return d

shania = make_album('Shania Twain', 'Up!')
print(shania)
m5 = make_album('Maroon 5', 'Songs About Jane', 12)
print(m5)

while True:
    artist = input("Please input the artist's name: "
                   "(enter 'q' at any time to quit): ")
    if artist == 'q':
        break
    album_title = input("Please input the album title: "
                        "(enter 'q' at any time to quit): ")
    if album_title == 'q':
        break
    my_album = make_album(artist, album_title)
    print(">> The dictionary created was:", my_album)
