# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# create dict

person = {
    'firstName': 'John',
    'lastName': 'Doe',
    'age': 30
}

#  Contstructor
# person2 = dict(firstName='Sara', lastName='Williams')

# Get a value
print(person['firstName'])

# Add value
person['phone'] = '555-555-5555'

# Get dict keys
print(person.keys())

# print(person)

# print(person2, type(person2))