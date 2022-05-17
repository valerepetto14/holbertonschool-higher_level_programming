#!/usr/bin/python3
class Square:
    '''define class square'''
    def __init__(self, size=0, position=(0, 0)):
        '''define constructor'''
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        '''getter of size'''
        return self.__position

    @size.setter
    def size(self, value):
        '''setter of size'''
        if len(value) != 2 or (value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value 
 
    def my_print(self):
        '''define method my_print that printed the square with #'''
        if (self.size == 0):
            print("")
        else:
            for d in range (self.__position[1]):
                print("")
            for i in range(self.size):
                for e in range(self.__position[0]):
                    print(" ", end="")
                for a in range(self.size):
                    print("#", end="")
                print("")
