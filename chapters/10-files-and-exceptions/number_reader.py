import json

filename = 'chapters/10-files-and-exceptions/numbers.json'
with open(filename) as f:
	numbers = json.load(f)

print(numbers)
print(type(numbers))
