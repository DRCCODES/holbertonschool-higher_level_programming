#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for el in matrix:
        for e in range(0, len(el)):
            if e < len(el) - 1:
                print("{:d} ".format(el[e]), end="")
            else:
                print("{:d}".format(el[e]))
        if len(el) <= 1:
            print()
