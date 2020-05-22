#!/usr/bin/python3
""" prints a square """

def print_square(size):
    sq = []
    
    if not isinstance(size,(int, float):
        raise TypeError("size must be an integer")
    elif is isinstance(size,(float) and size < 0):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise TypeError("size must be >= 0")

    for row in range(size):
        for columns in range(size):
            sq.append("#")
        if row != size - 1:
            sq.append("\n")
    print(''.join(sq))
