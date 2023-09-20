#!/usr/bin/python3
'''Module for Base Rectangle'''
from models.base import Base


class Rectangle(Base):
    '''Rectangle class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''constructor'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''get width of the rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        '''set width of the rectangle'''
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def heigth(self):
        '''get height of the rectangle'''
        return self.__height

    @heigth.setter
    def height(self, value):
        '''set height of the rectangle'''
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''get x of the rectangle'''
        return self.__x

    @x.setter
    def x(self, value):
        '''set x of the rectangle'''
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''get y of the rectangle'''
        return self.__y

    @y.setter
    def y(self, value):
        '''set y of the rectangle'''
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area value of the Rectangle."""
        return self.width * self.height

    def display(self):
	"""Print the Rectangle with the # character."""
        [print("") for y in range(self.y)]
        for i in range(self.height):
            print(" " * self.x, end="")
            [print("#", end="") for j in range(self.width)]
            print("")
