#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        tulpa_a += (0, 0)
    if len(tuple_b) < 2:
        tuple_b += (0, 0)
    ta = tuple_a
    tb = tuple_b
    tup = (ta[0] + tb[0], ta[1] + tb[1])
    return tup
