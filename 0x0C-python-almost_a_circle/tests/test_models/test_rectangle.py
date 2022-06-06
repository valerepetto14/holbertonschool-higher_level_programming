#!/usr/bin/python3
"""
test class rectangle
"""


from curses.textpad import rectangle
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class test_Rectangle(unittest.TestCase):
    """class rectangle test"""

    def test_id(self):
        """test id"""
        Base._Base__nb_objects = 0
        test2 = Rectangle(20, 2, 3, 12, 10)
        self.assertEqual(test2.id, 5)

    def test_rectangle_empty(self):
        """test rectangle empty"""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_rec_none(self):
        """Test if None args is given throws an error"""
        with self.assertRaises(TypeError):
            Rectangle(None)

    def test_datos(self):
        """def test datos"""
        with self.assertRaises(TypeError):
            test1 = Rectangle(["School", "Holberton"], 2)
        
        with self.assertRaises(TypeError):
            test1 = Rectangle([1,2], ["Holberton"], 2)
        
        with self.assertRaises(TypeError):
            test1 = Rectangle([], {}, 2)
        
        with self.assertRaises(TypeError):
            test1 = Rectangle("School", "Holberton", 2)

    def test_area(self):
        """def test method area"""
        self.assertEqual(Rectangle(3, 3).area(), 9)
        self.assertEqual(Rectangle(5, 5).area(), 25)

    def test_display(self):
        """def test display"""
        rec = rectangle(2,1)
        captureOutput = io.StringIO()
        sys.stdout = captureOutput
        rec.display()
        self.assertEqual(captureOutput.getvalue(), ("##\n##\n##\n"))
        

