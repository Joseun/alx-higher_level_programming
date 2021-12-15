#!/usr/bin/python3
"""Prints a name"""


def say_my_name(first_name, last_name=""):
    """Prints the first and last name in a sentence.

    Args:
        first_name(:obj:'str'): first name to be printed
        last_name(:obj:'str'): second name to be printed


     """
    if not type(first_name) is str:
        raise TypeError("first_name must be a string")

    if not type(last_name) is str:
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
