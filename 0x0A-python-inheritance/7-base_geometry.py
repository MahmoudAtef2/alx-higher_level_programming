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
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
