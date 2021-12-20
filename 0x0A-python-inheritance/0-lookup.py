#!/usr/bin/python3
"""Function to make a list of available attributes and methods"""


def lookup(obj):
    """Returns a list of available attributes and methods of an object"""

    return dir(obj)
