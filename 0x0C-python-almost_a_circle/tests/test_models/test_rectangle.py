#!/usr/bin/python3
"""Unit test class Rectangle"""
import unittest
import json
import sys
import os
from models.rectangle import Rectangle
from io import StringIO

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

    def test_rectangle(self):
        """
        Test check for rectangle
        """

        R1 = Rectangle(4, 5, 6)
        R1_dict = R1.to_dictionary()
        R2 = Rectangle.create(**R1_dict)
        self.assertNotEqual(R1, R2)

    def test_file_rectangle(self):
        """
        Test check if file loads from rectangle
        """

        R1 = Rectangle(33, 34, 35, 26)
        R2 = Rectangle(202, 2)
        lR = [R1, R2]
        Rectangle.save_to_file(lR)
        lR2 = Rectangle.load_from_file()
        self.assertNotEqual(lR, lR2)
