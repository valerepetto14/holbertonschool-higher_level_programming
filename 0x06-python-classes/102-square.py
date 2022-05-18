#!/usr/bin/python3
"""
define class square and
constructor with their variables and methods setter and getter
"""


class Square:
    """class square"""
    def __init__(self, size=0):
        """define constructor"""
        self.__size = size

    @property
    def size(self):
        """define method getter of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """define method setter of size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        "def area"
        return self.size * self.size

    def __eq__(self, other):
        """=="""
        return self.area() == other.area()

    def __ne__(self, other):
        """!="""
        return self.area() != other.area()

    def __lt__(self, other):
        """<"""
        return self.area() < other.area()

    def __le__(self, other):
        """<="""
        return self.area() <= other.area()

    def __gt__(self, other):
        """>"""
        return (self.area() > other.area())

    def __ge__(self, other):
        """>="""
        return (self.area() >= other.area())
