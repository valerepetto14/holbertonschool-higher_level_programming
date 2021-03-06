#!/usr/bin/python3
"""
Unitfor Square class
"""


from curses.textpad import rectangle
import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """def test square"""

    def test_size(self):
        """test size"""
        c1 = Square(10)
        self.assertEqual(c1.size, 10)
    
    def test_x(self):
        """test x"""
        c1 = Square(10,10,10,5)
        self.assertEqual(c1.x, 10)

    def test_y(self):
        """test y"""
        c1 = Square(10,10,10,5)
        self.assertEqual(c1.x, 10)

    def test_id(self):
        """test id"""
        c1 = Square(10,10,10,5)
        self.assertEqual(c1.id, 5)
 
    def test_update_kwargs(self):
        """test a part of update"""
        c1 = Square(10, 10, 10, 10)
        c1.update(id = 5)
        self.assertEqual(str(c1), "[Square] (5) 10/10 - 10")
    
    def test_to_dictionary(self):
        """test to_dictionary"""
        sdic = Square(1, 2, 3, 4).to_dictionary()
        s2 = Square(1, 2)
        s2.update(**sdic)
        self.assertEqual(str(s2), '[Square] (4) 2/3 - 1')