#!/usr/bin/python3
""" Doc for Class Student """


class Student:
    """ Student Class """

    def __init__(self, first_name, last_name, age):
        """ init for Student Class """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ returns dict of instance """
        if not isinstance(attrs, list):
            return self.__dict__

        for i in attrs:
            if not isinstance(i, str):
                return self.__dict__
        std = {}
        for things in attrs:
            if things in self.__dict__.keys():
                std[things] = self.__dict__[things]

        return std
