#!/usr/bin/python3
from models.base import Base
"""
Write the class Rectangle that inherits from Base:
"""


class Rectangle(Base):
    """def class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
            super().__init__(id)
            width = width
            height = height
            x = x
            y = y

    @property
    def width(self):
        """getter widht"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """setter width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value
    
    @property
    def height(self):
        """getter heigth"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """setter height"""
        if type(value) is not int:
             raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value
    
    @property
    def x(self):
        """getter x"""
        return self.__x
    
    @x.setter
    def x(self, value):
        """setter x"""
        if type(value) is not int:
             raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value
    
    @property
    def y(self):
        """getter widht"""
        return self.__y
    
    @y.setter
    def y(self, value):
        """setter y"""
        if type(value) is not int:
             raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    
    



