#!/usr/bin/python3
"""Function make addition of two numbers."""

def add_integer(a, b=98):
    """Adds two numbers a and b.
    
    Args:
        a: the first number.
        b: the second number, default 98.

    Raises:
        TypeError: If a or b is a non-integer and non-float.

    Returns:
        The addition of two numbers a and b.
    """

    if not isinstance(a, (int, float, bool)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float, bool)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
