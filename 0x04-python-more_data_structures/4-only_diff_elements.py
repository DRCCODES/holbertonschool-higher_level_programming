#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    nl = []
    for item in set_1:
        if item not in set_2:
            nl.append(item)
    for item in set_2:
        if item not in set_1:
            nl.append(item)
    return nl
