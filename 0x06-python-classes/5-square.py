#!/usr/bin/python3
class Square:
    '''define class square'''
    def __init__(self, size=0):
        '''define constructor'''
        self.__size = size

    @property
    def size(self):
        '''getter of size'''
        return self.__size

    @size.setter
    def size(self, value):
        '''setter of size'''
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        '''define method my_print that printed the square with #'''
        if (self.size == 0):
            print("")
        else:
            for i in range(self.size):
                print("")
                for a in range(self.size):
                    print("#", end="")
        print("")
