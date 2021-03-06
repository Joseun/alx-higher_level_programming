#!/usr/bin/python3
"""Printing a square"""


def print_square(size):
    """Print a square with character # using the arguement size as dimension.

    Args:
        size(:obj:'int'): size of the length of the square

     """


    if not type(size) is int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        print()
    else:
        for i in range(size):
            for j in range(size):
                print("{}".format("#"), end="")
            print()
