#!/usr/bin/python3
"""
returns True if the object is an instance of a class that inherited
 (directly or indirectly) from the specified class ; otherwise False
"""


from operator import truediv


def inherits_from(obj, a_class):
    """inherit from"""
    if (type(obj) != a_class) and (issubclass(type(obj), a_class) is True):
        return True
    else:
        return False
