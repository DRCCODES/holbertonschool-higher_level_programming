#!/usr/bin/python3

""" simple int adder """

def add_integer(a, b=98):

    """ Addeds a + b and returns results """

    if not isinstance(a,(int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b,(int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
