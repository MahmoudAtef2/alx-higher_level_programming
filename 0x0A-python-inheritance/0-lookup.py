#!/usr/bin/python3
'''Module for lookup method.'''


def lookup(obj):
    '''function return list of attributes and methods of an object
    Args:
        obj: the object.
    
    Returns:
        list: list of attributes and methods
    
    '''

    return dir(obj)
