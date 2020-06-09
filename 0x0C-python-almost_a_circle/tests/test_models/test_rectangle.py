#!/usr/bin/python3
""" Doc for Unittest of class Rectangle """

import sys
import io
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ Tests for class Rectangle """

    def test_docs(self):
        """ Tests Func Docs """
        self.assertTrue(len(Rectangle.__doc__) > 0)
        self.assertTrue(len(Rectangle.area.__doc__) > 0)
        self.assertTrue(len(Rectangle.display.__doc__) > 0)
        self.assertTrue(len(Rectangle.update.__doc__) > 0)
        self.assertTrue(len(Rectangle.to_dictionary.__doc__) > 0)

    def test_getter_setter_id(self):
        """ Test Setter, Getter and Id """

        Base._Base__nb_objects = 0

        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)


if __name__ == '__main__':
    unittest.main()
