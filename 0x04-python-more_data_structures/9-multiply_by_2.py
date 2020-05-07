#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    nd = {}
    for k, v in a_dictionary.items():
        nd[k] = v * 2
    return nd
