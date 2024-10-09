from datetime import timedelta, date, datetime
import math
import os
import random
import sys

# print(datetime.now())
# print(datetime.now().year)
# print(timedelta(days=100))
# print(math.pi)
# print(os.name)
# print(random.randint(1, 10))
# print(sys.argv)

print(date.today())
print(datetime.now())
print(timedelta(minutes=85))

# Import from a fmatg.py file
from fmath import sum, subtract, multiply, divide
sum(10, 20)
subtract(10, 20)
multiply(10, 20)
print(divide(10, 20))

# Colorama
from colorama import Fore, Back, Style
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')