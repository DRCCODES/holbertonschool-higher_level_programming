#!/usr/bin/python3
""" Doc for Unittest for class Square """


import unittest
import io
import sys
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """ Unittest for Class Square """

    def test_docs(self):
        """ Tests Func Docs """
        self.assertTrue(len(Square.__doc__) > 0)
        self.assertTrue(len(Square.update.__doc__) > 0)
        self.assertTrue(len(Square.to_dictionary.__doc__) > 0)
