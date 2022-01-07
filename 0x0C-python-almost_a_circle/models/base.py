#!/usr/bin/python3
"""Defining the class Base"""
import json


class Base:
    """This is an empty class that defines a square."""

    __nb_objects = 0

    def __init__(self, id=None):
        """This is the initialiazation function for Base

        Args:
            id(:obj:'int'): public instance

        """

        self.id = id
        if self.id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Method JSON string

        Args:
            - list_dictionaries: list of dicts

            Returns: JSON representation of the list
        """

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if (type(list_dictionaries) != list or
                not all(type(x) == dict for x in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation

        Args:
            - json_string: string to convert to list

        """

        my_list = []
        if json_string is not None and json_string != '':
            if type(json_string) != str:
                raise TypeError("json_string must be a string")
            my_list = json.loads(json_string)
        return my_list

    @classmethod
    def save_to_file(cls, list_objs):
        """JSON string representation

        Args:
            - list_objs: list of instances of Base

        """

        if list_objs is None or list_objs == []:
            my_list = "[]"
        else:
            my_list = cls.to_json_string([x.to_dictionary()
                                          for x in list_objs])
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            f.write(my_list)

    @classmethod
    def create(cls, **dictionary):
        """Returns a class instantied from a dictionary to initialize.

        Args:
           **dictionary (dict): dictionary pairs of attributes to initialize.

        """

        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings.
        Reads from `<cls.__name__>.json`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
