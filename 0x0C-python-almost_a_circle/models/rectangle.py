#!/usr/bin/python3
"""Defining the class Rectangle """
from models.base import Base


class Rectangle(Base):
    """Defines the class a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Intialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): private attribute
            y (int): private attribute

        """
        super().__init__(id)

        if not type(width) is int:
            raise TypeError('width must be an integer')
        elif width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

        if not type(height) is int:
            raise TypeError('height must be an integer')
        elif height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

        if not type(x) is int:
            raise TypeError('x must be an integer')
        elif x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

        if not type(y) is int:
            raise TypeError('y must be an integer')
        elif y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    @property
    def width(self):
        """Set/get the width of the Rectangle."""

        return self.__width

    @width.setter
    def width(self, width):
        """:obj:'int': Changes the width of the rectangle class"""

        if not type(width) is int:
            raise TypeError('width must be an integer')
        elif width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

    @property
    def height(self):
        """Set/get the height of the Rectangle."""

        return self.__height

    @height.setter
    def height(self, height):
        """:obj:'int': Changes the height of the rectangle class"""

        if not type(height) is int:
            raise TypeError('height must be an integer')
        elif height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    @property
    def x(self):
        """Set/get the x of the Rectangle."""

        return self.__x

    @x.setter
    def x(self, x):
        """:obj:'int': Changes the x-axis of the rectangle class"""

        if not type(x) is int:
            raise TypeError('x must be an integer')
        elif x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @property
    def y(self):
        """Set/get the y axis of the Rectangle."""

        return self.__y

    @y.setter
    def y(self, y):
        """:obj:'int': Changes the y-axis of the rectangle class"""

        if not type(y) is int:
            raise TypeError('y must be an integer')
        elif y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    def area(self):
        """:obj:'int': Returns the current rectangle area"""

        return self.__width * self.__height

    def display(self):
        """:obj:'int': Prints in standard output a rectangle with the character #

        """

        for i in range(self.__y):
            print()
        for j in range(self.__height):
            for k in range(self.__x):
                print("{}".format(" "), end="")
            for l in range(self.__width):
                print("{}".format("#"), end="")
            print()

    def __str__(self):
        """Returns to standard output the details of the rectangle"""

        return str("[Rectangle] ({}) {}/{} - {}/{}".
                   format(self.id, self.__x, self.__y, self.__width,
                          self.__height))

    def update(self, *args, **kwargs):
        """Updating the attributes of the Rectangle class

         Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute

        """
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.__width = args[1]
            if len(args) > 2:
                self.__height = args[2]
            if len(args) > 3:
                self.__x = args[3]
            if len(args) > 4:
                self.__y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                if key == "width":
                    self.__width = value
                if key == "height":
                    self.__height = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value

    def to_dictionary(self):
        """Defining the dictionary representation of a rectangle class"""

        my_dict = {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
        return my_dict
