#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
res = number % 10
if number < 0:
    number = number * -1
    res = number % 10
    res = res * -1
    number = number * -1
if (res > 5):
    print(f"Last digit of {number} is {res} and is greater than 5")
elif (res < 6 and res != 0):
    print(f"Last digit of {number} is {res} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is 0 and is 0")
