#!/usr/bin/python3
"""
Write the class Rectangle that inherits from Base:
"""
from models.base import Base


class Rectangle(Base):
    """def class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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

    def area(self):
        """def method area"""
        return self.width * self.height

    def display(self):
        """def method display"""
        if self.__width == 0:
            print('')
        else:
            for saltos in range(self.x):
                print()
            for height in range(self.__height):
                for spaces in range(self.y):
                    print(' ', end='')
                for width in range(self.__width):
                    print('#', end='')
                print("")

    def __str__(self):
        """def method str"""
        return ("[{}] ({}) {}/{} - {}/{}".format(
            self.__class__.__name__, self.id, self.x, self.y, self.width,
            self.height
        ))

    def update(self, *args, **kwargs):
        """def update"""
        atributos = ["id", "width", "height", "y", "x"]

        if len(args) != 0:
            for pos, arg in enumerate(args):
                if pos < (len(atributos) - 1):
                    setattr(self, atributos[pos], arg)
                else:
                    break
        else:
            for pos, arg in kwargs.items():
                setattr(self, pos, arg)

    def to_dictionary(self):
        """def to_dictionary"""
        dic = {}
        atributos = []
        for atributo in atributos:
            dic[atributo] = getattr(self, atributo)
        return dic
