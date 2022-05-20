#!/usr/bin/python3

def add_integer(a, b=98):
    """def add_integer that add two number"""
    if ((type(a) is not int or float) or (type(b) is not int or float)):
        raise TypeError("a must be an integer or b must be an integer")
    else:
        a = int(a)
        b = int(b)
        return a + b