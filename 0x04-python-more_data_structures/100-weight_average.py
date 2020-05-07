#!/usr/bin/python3
def weight_average(my_list=[]):
    p = 0
    s = 0
    if not my_list:
        return 0
    for x, y in my_list:
        p += x*y
        s += y
    if s == 0:
        return 0
    return p/s
