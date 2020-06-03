#!/usr/bin/python3
""" appends a file """


def append_write(filename="", text=""):
    """ apeend text to file """
    cn = len(text)

    with open(filename, mode='a') as f:
        aend = f.write(text)
    return cn
