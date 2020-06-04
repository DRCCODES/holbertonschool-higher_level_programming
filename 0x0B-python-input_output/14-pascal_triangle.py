#!/usr/bin/python3
""" pascal's list """


def pascal_triangle(n):
    """ Create Pascal's List """

    pr = [1]
    pt = []
    row = 0

    if n <= 0:
        return []

    pt.append(pr)

    if n == 1:
        return pt
    while row < n - 1:
        crow = []
        crow.append(pr[0])
        i = 0
        while i < row:
            crow.append(pr[i] + pr[i + 1])
            i += 1
        crow.append(pr[len(pr) - 1])
        pt.append(crow)
        pr = crow
        row += 1

    return pt
