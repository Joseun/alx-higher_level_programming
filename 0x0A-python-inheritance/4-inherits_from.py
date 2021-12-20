#!/usr/bin/python3
"""Check if instances of an object are inherited directly or indirectly"""


def inherits_from(obj, a_class):
    """Returns True if the object is an instance of a class that inherited
       directly or indirectly the specified class otherwise False

    Args:
        obj: object to look at
        a_class: class to varify the instance of

    Returns: True if obj is an instance of a_class, False otherwise
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
