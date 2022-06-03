#!/usr/bin/python3
from models.rectangle import Rectangle
"""
class square
"""


class Square(Rectangle):
    """def class Square that inherit of Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size ,size, y, x, id)
        
    def __str__(self):
        return f"[Square] ({self.id}) {self.y}/{self.x} - {self.width}"