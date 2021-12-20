#!/usr/bin/python3
"""Making an inherited class and sorting a list"""


class MyList(list):
    """This is a class inheriting properties from the 'list' object"""

    def print_sorted(self):
        """Returns a a sorted list of integers"""

        print(sorted(self))
