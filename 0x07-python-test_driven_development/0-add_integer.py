#!/usr/bin/python3

""" simple int adder """

def add_integer(a, b=98):

    """ Addeds a + b and returns results """

    if not isinstance(a,(int, b)):
        raise TypeError("b must be an integer")
    elif not isinstance(b,(int, a)):
        raise TypeError("a must be an integer")
    elif a is type(float):
        a = int(a)
    elif b is type(float):
        b = int(b)

    return a + b
