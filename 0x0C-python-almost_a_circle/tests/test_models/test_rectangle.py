#!/usr/bin/python3
""" Doc for Unittest of class Rectangle """

import sys
import io
import unittest
from models.base import Base
from models import rectangle
from models.rectangle import Rectangle

Rectangle = Rectangle
area = Rectangle.area
display = Rectangle.display
update = Rectangle.update
to_dictionary = Rectangle.to_dictionary


class TestRectangle(unittest.TestCase):
    """ Tests for class Rectangle """

    def test_docs(self):
        """ Tests Func Docs """
        self.assertTrue(len(rectangle.__doc__) > 0)
        self.assertTrue(len(Rectangle.__doc__) > 0)
        self.assertTrue(len(area.__doc__) > 0)
        self.assertTrue(len(display.__doc__) > 0)
        self.assertTrue(len(update.__doc__) > 0)
        self.assertTrue(len(to_dictionary.__doc__) > 0)

    def test_getter_setter_id(self):
        """ Test Setter, Getter and Id """

        capout = io.StringIO()
        Base._Base__nb_objects = 0
        sys.stdout = capout

        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)


if __name__ == '__main__':
    unittest.main()
