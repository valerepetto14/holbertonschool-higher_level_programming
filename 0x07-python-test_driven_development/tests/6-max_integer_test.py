#!/usr/bin/python3
"""
unisstest
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """def class"""
    
    def test_mayores(self):
        """Basic tests"""
        self.assertEqual(max_integer([1, 3, 4, 5]), 5)
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([1 ,3 ,55 , 100]), 100)
        self.assertEqual(max_integer([-1 ,-3 ,55 , -100]), 55)
    
    def test_none(self):
        self.assertIsNone(max_integer([]))
        self.assertIsNone(max_integer())
    
    def test_str(self):
        self.assertEqual(max_integer(["1","3"]), "3")
        self.assertEqual(max_integer(["h", "a"]), "h")


    

if __name__ == '__main__':
    unittest.main()
    