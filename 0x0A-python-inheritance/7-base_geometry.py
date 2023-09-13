#!/usr/bin/python3
'''Model for BaseGeometry calss'''


class BaseGeometry:
    '''BaseGeometry calss'''

    def area(self):
        '''area method'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''Method that validates value'''
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
