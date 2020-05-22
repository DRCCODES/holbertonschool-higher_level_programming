#!/usr/bin/python3
""" Divides a matrix """


def matrix_divided(matrix, div):
    nm = []
    size = len(matrix[0])

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if isinstance(matrix, list):
        for a in matrix:
            if not isinstance(a, (list)):
                raise TypeError("matrix must be a matrix (list of lists) \
                        of integers/floats")
            if len(a) != size:
                raise TypeError("Each row of the matrix must \
                        have the same size")
            for i in a:
                if not isinstance(i, (int, float)) or isinstance(i, tuple):
                    raise TypeError("matrix must be a matrix (list of lists) \
                            of integers/floats")
    for num in matrix:
        nm.append(list(map(lambda x: round(x / div, 2), num)))
    return nm
