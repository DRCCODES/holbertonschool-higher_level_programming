#!/usr/bin/python3
""" Doc for Unittest of class Base """


import unittest
import pep8
from models.base import Base



class TestBaseClass(unittest.TestCase):
    """ TestBaseClass to test Base Class """

    def test_class_doc(self):
        """ Test Class for Doc """

        self.assertTrue(len(Base.__doc__) > 0)

    def test_func_doc(self):
        """ Test all Func for Docs """

        self.assertTrue(len(Base.to_json_string.__doc__) > 0)
        self.assertTrue(len(Base.save_to_file.__doc__) > 0)
        self.assertTrue(len(Base.from_json_string.__doc__) > 0)
        self.assertTrue(len(Base.create.__doc__) > 0)
        self.assertTrue(len(Base.load_from_file.__doc__) > 0)

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

    def test_pep8(self):
        """ Test Pep Checks? """

        pepboy = pep8.StyleGuide(quiet=True)
        fallout = pepboy.check_files(["models/base.py"])
        self.assertEqual(fallout.total_errors, 0)

if __name__ == '__main__':
    unittest.main()
