#!/usr/bin/python3
""" function checks if obj instance
inherited from specific class True or False """


def inherits_from(obj, a_class):
    """ True if passes False if fales inheritence check """

    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
