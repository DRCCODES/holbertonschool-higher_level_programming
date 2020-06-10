#!/usr/bin/python3
""" Doc for Unittest of class Rectangle """

import sys
import io
import unittest
import pep8
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

        self.assertEqual(r1.width, 10)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r3.width, 10)

        self.assertEqual(r1.height, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r3.height, 2)

        self.assertEqual(r1.x, 0)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r3.x, 0)

        self.assertEqual(r1.y, 0)
        self.assertEqual(r2.y, 0)
        self.assertEqual(r3.y, 0)

        r4 = Rectangle(1, 1, 1, 1)
        self.assertEqual(r4.x, 1)
        self.assertEqual(r4.y, 1)

    def test_area_rec(self):
        """Test Area """

        Base._Base__nb_objects = 0

        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    def test_pep8(self):
        """ Test Pep Checks? """

        pepboy = pep8.StyleGuide(quiet=True)
        fallout = pepboy.check_files(["models/rectangle.py"])
        self.assertEqual(fallout.total_errors, 0)

if __name__ == '__main__':
    unittest.main()
