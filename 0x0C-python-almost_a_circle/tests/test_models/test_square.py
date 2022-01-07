#!/usr/bin/python3
"""Unit test class Square"""
import unittest
from models.square import Square
import sys
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

    def test_square(self):
        """
        Test check for square creation
        """

        S1 = Square(44, 55, 66, 77)
        S1_dict = S1.to_dictionary()
        S2 = Square.create(**S1_dict)
        self.assertNotEqual(S1, S2)

    def test_file_square(self):
        """
        Test check if file loads from square
        """

        S1 = Square(22)
        S2 = Square(44, 44, 55, 66)
        lS = [S1, S2]
        Square.save_to_file(lS)
        lS2 = Square.load_from_file()
        self.assertNotEqual(lS, lS2)
