#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a += (0, 0)
    tuple_b += (0, 0)
    ta = tuple_a[0] + tuple_b[0]
    tb = tuple_a[1] + tuple_b[1]
    tup = (ta, tb)
    return tup
