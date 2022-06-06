#!/usr/bin/python3
"""
TEST OF CLASS BASE
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """def class TestBase"""

    def Test_id(self):
        """test id"""
        def test_print(self):
            self.assertEqual(Base(1), self.id == 1)
            self.assertEqual(Base(1000), self.id == 1000)
            self.assertEqual(Base(3), self.id == 3)

    def Test_type(self):
        self.assertEqual(str(type(Base)), "<class 'type'>")
        self.assertEqual(str(type(Rectangle)), "<class 'type'>")
        self.assertEqual(str(type(Square)), "<class 'type'>")
    
    def Test_to_json_string(self):
        """test method to json string"""
        new_dictionary =  {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        new_json_string = Base.to_json_string([new_dictionary])
        self.assertEqual(new_json_string, '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]')
    