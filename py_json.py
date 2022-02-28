# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary


import json

# Simple JSON
userJson = '{"firstName": "mubarak", "lastName": "jama", "age": 30}'

# parse it to dict
user = json.loads(userJson)

# print(user)
# print(user['firstName'])

car = {
    'make': 'ford',
    'model': 'mustang',
    'year': 1970
}

carJSON = json.dumps(car)

print(carJSON)
