#!/usr/bin/python3
""" doc for fun check if obj instance of class or instance of inherited """


def is_kind_of_class(obj, a_class):
    """ check obj for instance of class of if inheriated from class """

    if isinstance(obj, a_class):
        return True
    else:
        return False
