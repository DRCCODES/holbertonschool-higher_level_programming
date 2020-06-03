#!/usr/bin/python3
""" adds new attribute if able """


def add_attribute(obj, name, value):
    """ checks and adds attr """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
