# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# creating class
class User:
    # constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
    
    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'
    
    def has_birthday(self):
        self.age += 1 

# Extend class

class Customer(User): 
    # constructor 
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def setBalance(self, balance):
        self.balance = balance
    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'
    

# init user object
brad = User('Brad', 'brad@gmail.com', 37)

# Init customer
jane = Customer('Jane', 'jane@gmail.com', 25)

jane.setBalance(500)

brad.has_birthday()

print(jane.greeting())


# print(type(brad))