#!/usr/bin/python3
"""Addition function of two integers"""


def add_integer(a, b=98):
    """Return the result of a and b as an integer.

    Args:
        a(:obj:'int', 'float'): first argument
        b(:obj:'int', 'float'): second argument

     """

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if not type(a) is int:
        raise TypeError("a must be an integer")
    if not type(b) is int:
        raise TypeError("b must be an integer")
    return a + b
