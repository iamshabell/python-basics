# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

import datetime
from datetime import date
import email
import time
from time import time

# pip module
from camelcase import CamelCase

# custom
import validator
from validator import validate_email


# today
today = date.today()
timestamp = time()


c = CamelCase()
# print(c.hump('hello there world'))

email = 'test@gmail.com'
if validate_email(email):
    print('Email is valid')
else:
    print('Email is not valid')

# print(timestamp)
