#!/usr/bin/python3
"""
inherits from list and method that prints the list
"""


class MyList(list):
    """sub class"""
    pass

    def print_sorted(self):
        """print list"""
        print(sorted(self))
