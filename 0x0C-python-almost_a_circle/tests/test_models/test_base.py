#!/usr/bin/python3
from re import M
import unittest
from pyrsistent import b
from models import base
from models import rectangle
base = base.Base
rectangle = rectangle.Rectangle
"""
TEST OF CLASS
"""


class TestStringMethods(unittest.TestCase):
    """test print"""
    def test_print(self):
        self.assertEqual(base(1), self.id == 1)