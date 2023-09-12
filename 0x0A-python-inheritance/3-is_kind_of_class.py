#!/usr/bin/python3
'''function that check if an object is instance of a class 
or calss that inherited from'''


def is_kind_of_class(obj, a_class):
    '''check the object.
    Args:
        obj: the object to check.
        a_class: the class to check.

    Returns:
        True or Fals.
    '''
    if isinstance(obj, a_class):
        return True
    else:
        return False
