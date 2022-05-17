#!/usr/bin/python
class Square:
    '''class square'''
    def __init__(self, size=0):
        '''hacemos el construcctor'''
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        '''metodo que calcula el area'''
        return self.__size * self.__size
