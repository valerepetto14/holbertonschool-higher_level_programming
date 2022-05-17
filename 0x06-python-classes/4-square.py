#!/usr/bin/python3
"""
define class square and constructor with their variables and methods setter and getter
"""

class Square:
    '''define class square'''
    def __init__(self, size=0):
        '''define constructor'''
        self.__size = size

    @property
    def size(self):
        '''define method getter of size'''
        return self.__size

    @size.setter
    def size(self, value):
        '''define method setter of size'''
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        '''define method that calc the area of square'''
        return self.size * self.size
