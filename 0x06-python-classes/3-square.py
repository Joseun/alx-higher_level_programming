#!/usr/bin/python3
"""Creating the class Square"""


class Square:
    """This is an empty class that defines a square"""

    def __init__(self, size=0):
        """This is an empty class that defines a square of size 'size

        Args:
            size(:obj:'int'): paramter to determine the size of the square.

        """

        if not type(size) is int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size  #: Size of the square.

    def area(self):
        """:obj:'int': Returns the current square area"""

        return (self.__size * self.__size)
