#!/usr/bin/python3
"""
def add_integer
"""


def print_square(size):
    """print square"""
    if (type(size) != int):
        raise TypeError("size must be an integer")
    elif (size < 0):
        raise ValueError("size must be >= 0")
    for i in range(size):
        for a in range(size):
            print("#",end="")
        print("")