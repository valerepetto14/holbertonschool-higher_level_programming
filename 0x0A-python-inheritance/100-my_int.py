#!/usr/bin/python3
"""
Write a class MyInt that inherits from int:

MyInt is a rebel. MyInt has == and != operators inverted
You are not allowed to import any module
"""


class MyInt(int):
    """def class MyInt"""
    def __init__(self, value):
        """def init"""
        self.value = value

    def __eq__(self, value):
        """def eq"""
        return "False"

    def __ne__(self, value):
        """def ne"""
        return True
