#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nl = []
    for item in my_list:
        if item == search:
            nl.append(replace)
        else:
            nl.append(item)
    return(nl)
