import json

numbers = {'numbers': [2, 3, 5, 7, 11, 13]}

filename = 'chapters/10-files-and-exceptions/numbers.json'
with open(filename, 'w') as f:
	json.dump(numbers,f)
