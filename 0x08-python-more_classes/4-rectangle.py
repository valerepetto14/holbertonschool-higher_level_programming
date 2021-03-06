#!/usr/bin/python3
"""
create rectangle
"""


class Rectangle:
    "def class rectangle"
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__heigth

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__height = value

    def area(self):
        "def method that calc area"
        return self.__width * self.__height

    def perimeter(self):
        "def method that calc perimetro"
        if self.width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        string = ""
        """Prints in stdout the square with the character #"""
        if self.__width == 0:
            return string
        else:
            for height in range(self.__height):
                for width in range(self.__width):
                    string += "#"
                string += "\n"
        return string[:-1]

    def __repr__(self):
        "def repr"
        return f"Rectangle({self.__width}, {self.__height})"
