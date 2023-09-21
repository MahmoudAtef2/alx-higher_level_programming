#!/usr/bin/python3
'''Module for Base Rectangle'''
from models.base import Base


class Square(Rectangle):
    '''Square class'''

    def __init__(self, size, x=0, y=0, id=None):
        '''constructor'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''method that return info about Square'''
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        '''get size of the square'''
        return self.width

    @size.setter
    def size(self, value):
        '''set size of the square'''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''method that updates attributes via *args or **kwargs'''
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return dictionary representation of a Rectangle"""
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}
