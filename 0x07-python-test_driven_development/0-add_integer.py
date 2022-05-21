#!/usr/bin/python3

def add_integer(a, b=98):
    """def add_integer that add two number"""
    if (type(a) is not int and type(a) is not float):
        raise TypeError("a must be an integer")
    elif (type(b) is not int and type(b) is not float):
        raise TypeError("b must be an integer")
    else:
        a = int(a)
        b = int(b)
        return a + b
