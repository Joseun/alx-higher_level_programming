#!/usr/bin/python3
"""
This module contains all unittest for Base class
"""
import unittest
from models.square import Square
import sys
from io import StringIO
from models.base import Base
import json
from models.rectangle import Rectangle
import os


class TestBase(unittest.TestCase):
    """
    Class of functions to run tests
    """
    def setUp(self):
        """
        function to redirect stdout
        """
        sys.stdout = StringIO()

    def tearDown(self):
        """
        cleans everything
        """
        sys.stdout = sys.__stdout__

    def test_01_id(self):
        """
        Test check for id
        """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)

    def test_02_from_json_string(self):
        """
        Test check from json string
        """
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        with self.subTest():
            r1 = Rectangle(10, 7, 2, 8, 1)
            r1_dict = r1.to_dictionary()
            json_dict = Base.to_json_string([r1_dict])
            self.assertEqual(r1_dict, {'x': 2, 'width': 10,
                                       'id': 1, 'height': 7,
                                       'y': 8})
            self.assertIs(type(r1_dict), dict)
            self.assertIs(type(json_dict), str)
            self.assertEqual(json.loads(json_dict), json.loads('[{"x": 2, '
                                                               '"width": 10, '
                                                               '"id": 1, '
                                                               '"height": 7, '
                                                            '"y": 8}]'))
