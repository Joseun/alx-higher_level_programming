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

    @property
    def size(self):
        """:obj:'int': Retrieves the size of the square"""

        return self.__size

    @size.setter
    def size(self, value):
        """:obj:'int': Changes the size of the square"""

        if not type(value) is int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """:obj:'int': Returns the current square area"""

        return (self.__size * self.__size)
