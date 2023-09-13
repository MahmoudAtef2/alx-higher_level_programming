#!/usr/bin/python3
'''Model for BaseGeometry calss'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Rectangle method'''

    def __init__(self, width, height):
        '''Constructor'''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''Method that return the area rectangle'''
        return self.__width * self.__height

    def __str__(self):
        '''str reoresentation'''
        return f"[Rectangle] {str(self.__width)}/{str(self.__height)}"
