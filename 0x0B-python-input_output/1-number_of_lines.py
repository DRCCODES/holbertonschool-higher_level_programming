#!/usr/bin/python3
""" counts line in file """


def number_of_lines(filename=""):
    """ count number of lines in file """
    l = 0

    with open(filename) as f:
        for lines in f:
            l += 1
    return l
