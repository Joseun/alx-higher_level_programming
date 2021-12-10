#!/usr/bin/python3
"""Creating the class Square"""


class Square:
    """This is an empty class that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """This is an empty class that defines a square of size 'size

        Args:
            size(:obj:'int'): parameter to determine the size of the square.
            position(:obj:'tuple'): parameter to determine the
                  position of a point in the square.

        """

        if not type(size) is int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size  #: Size of the square.

        if not type(position) is tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif not len(position) == 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif not type(position[0]) or type(position[1]) is int:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif position[0] or position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = position  #: Position of a point in the square

    @property
    def size(self):
        """:obj:'int': Retrieves the size of the square"""

        return self.__size

    @property
    def position(self):
        """:obj:'tuple': Retrieves a position in the square"""

        return self.__position

    @size.setter
    def size(self, value):
        """:obj:'int': Changes the size of the square"""

        if not type(value) is int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @position.setter
    def position(self, value):
        """:obj:'tuple': Changes a position in the square"""

        if not type(value) is tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif not len(position) == 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif not type(position[0]) or type(position[1]) is int:
            raise TypeError('position must be a tuple of 2 positive integers')
        elif position[0] or position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """:obj:'int': Returns the current square area"""

        return (self.__size * self.__size)

    def my_print(self):
        """:obj:'int': Prints in standard outpur a square with the character #
        """
        if self.__size == 0:
            print()

        for i in range(self.__position[1]):
            print()
        for j in range(self.__size):
            for k in range(self.__position[0]):
                print("{}".format(" "), end="")
            for l in range(self.__size):
                print("{}".format("#"), end="")
            print()
