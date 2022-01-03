#!/usr/bin/python3
"""Defining the class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This is class that defines a Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Intialize a new Square.

        Args:
            size (int): The size of the new square.
            x (int): private attribute
            y (int): private attribute

        """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Set/get the size of square."""

        return self.width

    @size.setter
    def size(self, value):
        """:obj:'int': Changes the height of the square class"""

        if not type(value) is int:
            raise TypeError('size must be an integer')
        elif value <= 0:
            raise ValueError('size must be > 0')
        self.width = value
        self.height = value

    def __str__(self):
        """Returns to standard output the details of the square"""

        return str("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                        self.y, self.size))

    def update(self, *args, **kwargs):
        """Updating the attributes of the Square class

         Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represent x attribute
                - 4th argument represents y attribute

        """
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Defining the dictionary representation of a rectangle class"""

        my_dict = {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
        return my_dict
