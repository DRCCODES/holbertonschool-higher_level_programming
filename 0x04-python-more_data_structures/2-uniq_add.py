#!/usr/bin/python3
def uniq_add(my_list=[]):
    nl = []
    i = 0
    for item in my_list:
        if item not in nl:
            i += item
            nl.append(item)
    return(i)
