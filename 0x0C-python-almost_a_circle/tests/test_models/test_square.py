#!/usr/bin/python3
"""
Unitfor Square class
"""


import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """def test square"""

    def test_size(self):
        """test size"""
        c1 = Square(10)
        self.assertEqual(c1.size, 10)

def test_update_kwargs(self):
        """test a part of update"""
        c1 = Square(10, 10, 10, 10)
        c1.update(id = 5)
        self.assertEqual(str(c1), "[Square] (5) 10/10 - 10")