#!/usr/bin/python3
""" write to file """


def write_file(filename="", text=""):
    """ writes to file """

    with open(filename, mode="w") as f:
        right = f.write(text)
    return right
