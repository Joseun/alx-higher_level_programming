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
