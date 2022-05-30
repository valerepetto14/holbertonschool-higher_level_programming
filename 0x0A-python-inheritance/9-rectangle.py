#!/usr/bin/python3
"""
Write a class Rectangle that inherits from BaseGeometry
(7-base_geometry.py). (task based on 8-rectangle.py)

Instantiation with width and height: def __init__(self, width, height)::
width and height must be private. No getter or setter
width and height must be positive integers validated by integer_validator
the area() method must be implemented
print() should print, and str() should return, the following rectangle
 description:
 [Rectangle] <width>/<height>
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle (BaseGeometry):
    """def class BaseGeometry"""
    def __init__(self, width, height):
        """def  init"""
        self.__height = self.integer_validator("height", height)
        self.__width = self.integer_validator("width", width)

    def area(self):
        """def area"""
        return self.__width * self.__height

    def __str__(self):
        """def __str__"""
        return f"[{type(self).__name__}] {self.__width}/{self.__height}"
