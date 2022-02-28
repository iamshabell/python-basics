# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Mubarak'
age = 19

# Concatenate
# print('Hello, my name is ' + name + " and I'm " + str(age) + " yrs old")

# String Formatting

# Arguments by position
# print('My name is {name} and I am {age}'.format(name=name, age=age))

# F-Strings (3.6+)
# print(f'my name is {name} and I am {age}')


# String Methods

s = "hello world"

# Capitalize string
print(s.capitalize())
print(s.split())
print(len(s))  # Get Length