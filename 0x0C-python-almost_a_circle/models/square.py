#!/usr/bin/python3
from models.rectangle import Rectangle
"""
class square
"""


class Square(Rectangle):
    """def class Square that inherit of Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size ,size, x, y, id)
        
    @property
    def size(self):
        """def getter size"""
        return self.width
    
    @size.setter
    def size(self, value):
        """def setter size"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """def method update"""
        attrs = ["id", "size", "x", "y"]

        if len(args) != 0:
            for position, arg in enumerate(args):
                if position <= (len(attrs) - 1):
                    setattr(self, attrs[position], arg)
                else:
                    break 
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        It returns a dictionary representation of a Square
        :return: A dictionary with the id, x, size, and y of the square
        """
        return {"id": self.id, "x": self.x , "size" : self.size , "y": self.y}