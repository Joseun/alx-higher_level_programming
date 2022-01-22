#!/usr/bin/python3
"""Creating the class Rectangle"""


class Rectangle:
    """This is an empty class that defines a Rectangle."""

    def __init__(self, width=0, height=0):
        """This is an empty class that defines a square of size 'size

        Args:
            width: parameter to determine the width of the rectangle.
            height: parameter to determine the height of the rectangle.

        """

        if not type(width) is int:
            raise TypeError('width must be an integer')
        elif width < 0:
            raise ValueError('width must be >= 0')
        if not type(height) is int:
            raise TypeError('height must be an integer')
        elif height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height
        self.__width = width

        @property
        def width(self):
            """Set/get the width of the Rectangle."""

            return self.__width

        @width.setter
        def width(self, value):
            """:obj:'int': Changes the width of the rectangle class"""

            if not type(value) is int:
                raise TypeError('width must be an integer')
            elif value < 0:
                raise ValueError('width must be >= 0')
            self.__width = value

        @property
        def height(self):
            """Set/get the height of the Rectangle."""

            return self.__height

        @height.setter
        def height(self, value):
            """:obj:'int': Changes the height of the rectangle class"""

            if not type(value) is int:
                raise TypeError('height must be an integer')
            elif value < 0:
                raise ValueError('height must be >= 0')
            self.__height = value
