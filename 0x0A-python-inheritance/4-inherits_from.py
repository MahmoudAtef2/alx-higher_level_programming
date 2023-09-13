#!/usr/bin/python3
'''function that check if an object is instance of calss that inherited from'''


def inherits_from(obj, a_class):
    '''check the object.
    Args:
        obj: the object to check.
        a_class: the class to check.

    Returns:
        True or Fals.
    '''
    return isinstance(obj, a_class) and type(obj) != a_class
