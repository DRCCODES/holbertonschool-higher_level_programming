#!/usr/bin/python3
""" reads file """


def read_file(filename=""):
    """ function that reads a file """

    with open(filename) as f:
        for line in f:
            print(line, end="")
