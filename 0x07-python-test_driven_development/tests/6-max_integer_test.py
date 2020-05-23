#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Class to test max_integer funtion"""

    def test_docs(self):
        self.assertTrue(len(__import__("6-max_integer").__doc__) > 0)
        self.assertTrue(len(max_integer.__doc__) > 0)

    def test_ints(self):
        """ Testing ints """
        check_list = [1, 2, 3, 4]
        self.assertEqual(max_integer(check_list), 4)

        check_list = [-1, -2, -3, -4]
        self.assertEqual(max_integer(check_list), -1)

        check_list = [0, 0, 0, 0]
        self.assertEqual(max_integer(check_list), 0)

        check_list = [1, 2, 3, 40000000000000]
        self.assertEqual(max_integer(check_list), 40000000000000)

        check_list = [1, 2, 30000000000, 4]
        self.assertEqual(max_integer(check_list), 30000000000)

        check_list = [7, 4, 4, 7.1]
        self.assertEqual(max_integer(check_list), 7.1)

    def test_empty(self):
        """ Test Emptyness """
        check_empty = []
        self.assertEqual(max_integer(check_empty), None)

    def test_errors(self):
        """ checking simple errors """
        test_list = [1, "Super Fighting Robot", "Mazinger Man", 4]
        self.assertRaises(TypeError)


if __name__ == '__main__':
    unittest.main()
