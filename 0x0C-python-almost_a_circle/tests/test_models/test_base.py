#!/usr/bin/python3
""" Doc for Unittest of class Base """


import unittest
from models import base
from models.base import Base


to_json_string = Base.to_json_string
save_to_file = Base.save_to_file
from_json_string = Base.from_json_string
create = Base.create
load_from_file = Base.load_from_file


class TestBaseClass(unittest.TestCase):
    """ TestBaseClass to test Base Class """

    def test_doc(self):
        """ Test for Doc """

        self.assertTrue(len(base.__doc__) > 0)

    def test_class_doc(self):
        """ Test Class for Doc """

        self.assertTrue(len(Base.__doc__) > 0)

    def test_func_doc(self):
        """ Test all Func for Docs """

        self.assertTrue(len(to_json_string.__doc__) > 0)
        self.assertTrue(len(save_to_file.__doc__) > 0)
        self.assertTrue(len(from_json_string.__doc__) > 0)
        self.assertTrue(len(create.__doc__) > 0)
        self.assertTrue(len(load_from_file.__doc__) > 0)

    """ id tests """

    def test_id(self):
        """ Test id count """
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base().id, 3)
        self.assertEqual(Base().id, 4)
        self.assertEqual(Base().id, 5)
        self.assertEqual(Base().id, 6)
        self.assertEqual(Base().id, 7)
        bas = Base(100)
        self.assertEqual(bas.id, 100)


if __name__ == '__main__':
    unittest.main()
