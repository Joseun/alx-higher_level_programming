#!/usr/bin/python3
"""Check if instances of an object are the same"""


def is_same_class(obj, a_class):
    """Returns True if the object is exactly an instance of the specified class
       otherwise False

    Args:
        obj: object to look at
        a_class: class to varify the instance of

    Returns: True if obj is an instance of a_class, False otherwise
    """

    if type(obj) is a_class:
        return True
    return False
