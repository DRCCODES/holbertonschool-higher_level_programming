#!/usr/bin/python3
""" read n num of lins and print to stdout """


def read_lines(filename="", nb_lines=0):
    """ reads n num lines and prints """
    l = 0
    with open(filename, encoding="utf-8") as f:
        for lines in f:
            l += 1
        f.seek(0)
        if nb_lines <= 0 or nb_lines >= l:
            print(f.read(), end="")
        else:
            for n in range(nb_lines):
                print(f.readline(), end="")
