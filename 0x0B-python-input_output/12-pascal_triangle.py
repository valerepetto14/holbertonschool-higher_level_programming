#!/usr/bin/python3
"""
Technical interview preparation:

You are not allowed to google anything
Whiteboard first
Create a function def pascal_triangle(n): that returns a list
 of lists of integers representing the Pascal’s triangle of n:

Returns an empty list if n <= 0
You can assume n will be always an integer
You are not allowed to import any module
"""


def pascal_triangle(n):
    res = []
    """def pascal_triangle"""
    for i in range(n):
        niveles = []
        if i is 0:
            niveles.append(1)
            res = res + niveles
        else:
            for a in range(i):
                niveles

        