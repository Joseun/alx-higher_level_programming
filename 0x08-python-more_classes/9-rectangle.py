#!/usr/bin/python3
"""Creating the class Rectangle"""


class Rectangle:
    """This is an empty class that defines a Rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    @classmethod
    def square(cls, size=0):
        """
        Returns a new Rectangle instance with width == height == size
        """

        if not type(size) is int:
            raise TypeError('size must be an integer')
        width = size
        height = size
        return cls(width, height)

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
        self.__width = width

        if not type(height) is int:
            raise TypeError('height must be an integer')
        elif height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """:obj:'int': Returns the current rectangle area"""

        return (self.__width * self.__height)

    def perimeter(self):
        """:obj:'int': Returns the current rectangle perimeter"""

        if self.__width and self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        """
        :obj:'int': Prints in standard output a square with the character
        stored in print_symbol attribute

        """

        for i in range(self.__height):
            for j in range(self.__width):
                print("{}".format(self.print_symbol), end="")
            if i != self.__height - 1:
                print('')
        return ''

    def __repr__(self):
        """
        Returns to standard output the width and height
        """

        return str("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """
        Prompts an instance being deleted
        """

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the biggest rectangle based on the area

        Args:
        rect_1: first rectangle.
        rect_2: second rectangle.
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')

        if Rectangle.area(rect_1) == Rectangle.area(rect_2):
            return rect_1
        elif Rectangle.area(rect_1) > Rectangle.area(rect_2):
            return rect_1
        else:
            return rect_2
