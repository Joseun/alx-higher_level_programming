#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        list_used = [2, 6, 1, 4]
        self.assertEqual(max_integer(list_used), 6)

if __name__ == '__main__':
    unittest.main()
