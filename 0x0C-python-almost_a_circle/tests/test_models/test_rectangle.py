#!/usr/bin/python3
'''
Unittest for rectangle class
'''


from curses.textpad import rectangle
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class test_Rectangle(unittest.TestCase):
    '''class'''

    def test_id(self):
        '''testeamos id'''
        Base._Base__nb_objects = 0
        test2 = Rectangle(20, 2, 3, 12, 10)
        self.assertEqual(test2.id, 5)

    def test_rectangle_empty(self):
        """
        Test if too little args given throws an error
        """
        with self.assertRaises(TypeError):
            Rectangle()

    def test_rec_none(self):
        """
        Test if None args is given throws an error
        """
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
        
    def test_display(self):
        """def test display"""
        rec = rectangle(2,1)
        captureOutput = io.StringIO()
        sys.stdout = captureOutput
        rec.display()
        self.assertEqual(captureOutput.getvalue(), ("##\n##\n##\n"))
        

