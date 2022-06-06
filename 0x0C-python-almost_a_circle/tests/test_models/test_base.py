#!/usr/bin/python3
"""
TEST OF CLASS BASE
"""


import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class test_Base(unittest.TestCase):
    """def class TestBase"""
    def test_id(self):
        """test id"""
        def test_print(self):
            self.assertEqual(Base(1), self.id == 1)
            self.assertEqual(Base(1000), self.id == 1000)
            self.assertEqual(Base(3), self.id == 3)

    def test_type(self):
        """def method test_type"""
        self.assertEqual(str(type(Base)), "<class 'type'>")
        self.assertEqual(str(type(Rectangle)), "<class 'type'>")
        self.assertEqual(str(type(Square)), "<class 'type'>")
    
    def test_to_json_string(self):
        """test method to json string"""
        new_dictionary =  {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        new_json_string = Base.to_json_string([new_dictionary])
        self.assertEqual(new_json_string, '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]')
    
    def test_base_class(self):
        """def test for type"""
        b1 = Base()
        self.assertEqual(type(b1), Base)
        self.assertEqual(issubclass(Rectangle, Base), True)
        self.assertEqual(issubclass(Square, Base), True)
        self.assertEqual(issubclass(Rectangle, Square), False)
        self.assertEqual(issubclass(Square, Rectangle), True)
    
    def test_save_to_file(self):
        """def test save to file"""
        with self.assertRaises(AttributeError):
            Base.save_to_string()
    
    

    