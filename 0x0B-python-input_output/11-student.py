#!/usr/bin/python3
""" Doc for Class Student """


class Student:
    """ Student Class """

    def __init__(self, first_name, last_name, age):
        """ init for Student Class """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ returns dict of instance """

        return self.__dict__
