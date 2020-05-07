#!/usr/bin/python3
def common_elements(set_1, set_2):
    nl = []
    for item in set_1:
        if item in set_1 and item in set_2:
            nl.append(item)
    return nl
