#!/usr/bin/python3
"""Creating the class BaseGeometry"""


class BaseGeometry:
    """This is class that defines a BaseGeometry."""

    def area(self):
        """Raises an exception"""


        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """This is an function that validates an integer


        Args:
            name(:obj:'str'): parameter to determine the name.
            value(:obj:'int'): parameter to determine value

        """

        if not type(value) is int:
            raise TypeError('{} must be an integer'.format(name))
        elif value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))

        self.name = name
        self.value = value

class Rectangle(BaseGeometry):
    """This is class that defines a Rectangle"""

    def __init__(self, width, height):
        """This is an function that defines a rectangle


        Args:
            width(:obj:'int'): parameter to determine the width.
            height(:obj:'int'): parameter to determine height

        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Implements the area of a rectangle"""

        return (self.__width * self.__height)

    def __str__(self):
        """Returns to standard output the width and height

        """

        return str("[Rectangle] {}/{}".format(self.__width, self.__height))

class Square(Rectangle):
    """This is class that defines a Square"""

    def __init__(self, size):
        """This is an function that defines a square


        Args:
            size(:obj:'int'): parameter to determine the size of the square.

        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

