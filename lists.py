# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create a list
numbers = [1,2,3]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# constructor
# numbers2 = list((1,2,3))

# Get a value
# print(fruits[1])

# Get length
# print(len(fruits))

# Append to list or add
fruits.append('Mangoes')

# Remove from list
fruits.remove('Grapes')

# Insert into a postion
fruits.insert(2, 'Strawberry')

# Change value
fruits[0] = 'Blueberries'

# Remove with pop
fruits.pop(2)

# Reverse list
fruits.reverse()

# Sort list
fruits.sort()

# reverse sort
fruits.sort(reverse=True)

print(fruits)
