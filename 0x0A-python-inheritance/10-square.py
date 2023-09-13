#!/usr/bin/python3
'''Model for Rectangle calss'''
Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    '''subclass of rectangle class'''
    def __init__(self, size):
        '''constructor'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''Method that return the area of square'''
        return self.__size ** 2
