#!/usr/bin/python3
"""
define class rectangle and constructor
"""


class Rectangle:
    """creamos la clase"""
    def __init__(self, width=0, height=0):
        """creamos el constructor"""
        self.heigth = heigth
        self.width = width

    @property
    def width(self):
        '''private instance attribute named width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''setter of the private instance width'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''private instance attribute named height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''setter of the private instance height'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
