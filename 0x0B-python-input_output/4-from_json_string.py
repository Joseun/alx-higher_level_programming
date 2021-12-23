#!/usr/bin/python3
"""JSON reconversion to objects"""
import json


def from_json_string(my_str):
    """A function that returns a JSON representation of an object back to
    the original format

    Args:
        my_str (:obj:str): object to be converted
.
    Returns:
        the object.

    """

    return json.loads(my_str)
