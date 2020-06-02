#!/usr/bin/python3
""" function checks if obj is instance o class """


def is_same_class(obj, a_class):
    """ checks obj against class to see if instance of """

    if not type(obj) == a_class:
        return False
    else:
        return True
