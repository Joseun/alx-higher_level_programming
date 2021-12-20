#!/usr/bin/python3
"""Check if instances of an object are the same"""


def is_kind_of_class(obj, a_class):
    """Returns True if the object is kind of an instance of the specified class
       otherwise False

    Args:
        obj: object to look at
        a_class: class to varify the instance of

    Returns: True if obj is an instance of a_class, False otherwise
    """

    return isinstance(obj, a_class)
