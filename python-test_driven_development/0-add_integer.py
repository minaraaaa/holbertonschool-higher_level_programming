#!/usr/bin/python3
"""
This module provides a simple function to add two integers.
It checks for valid types (int, float) and casts them to integers
before performing the addition.
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a: The first parameter, must be an int or float.
        b: The second parameter, must be an int or float. Default is 98.

    Returns:
        The addition of a and b as an integer.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
