#!/usr/bin/python3
"""
create rectangle
"""


class Rectangle:
    """def class Rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """def init"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
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
        """Prints in stdout the square with the character #"""
        String = ""
        if self.__width == 0:
            return string
        else:
            for height in range(self.__height):
                for width in range(self.__width):
                    string += str(self.print_symbol)
                string += "\n"
        return string[:-1]

    def __repr__(self):
        "def repr"
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        "def del"
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """def bigger or equal"""
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1
        elif rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """des square"""
        cls = Rectangle(size, size)
        return cls
