#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list):
        return(None)
    cpy_list = []
    for item in my_list:
        cpy_list.append(item)
    cpy_list[idx] = element
    return(cpy_list)
