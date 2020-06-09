#!/usr/bin/python3
""" Doc for Unittest for class Square """


import unittest
import io
import sys
from models.base import Base
from models.rectangle import Rectangle
from models import square
from models.square import Square
Square = Square
update = Square.update
to_dictionary = Square.to_dictionary


class TestSquare(unittest.TestCase):
    """ Unittest for Class Square
