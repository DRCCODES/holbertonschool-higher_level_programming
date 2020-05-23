#!/usr/bin/python3
""" mutiples the matricies!!! """


def matrix_mul(m_a, m_b):
    """ Pythonicallys Doing things without numpy """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_a must be a list")
    for a in m_a:
        if not isinstance(a, (list)):
                raise TypeError(
                    "m_a must be a list of lists")
        if not len(m_a) or not len(a):
            raise ValueError(
                    "m_a can't be empty")
        for i in a:
            if not isinstance(i, (int, float)):
                    raise TypeError(
                        "m_a should contain only integers or floats")
            if len(m_a[0]) != len(a):
                raise ValueError(
                    "m_a and m_b can't be multiplied")
    for b in m_b:
        if not isinstance(b, list):
            raise TypeError(
                    "m_b must be a list of list")
        if not len(m_a) or not len(b):
            raise ValueError("m_b can't be empty")
        for j in b:
            if not isinstance(j, (int, float)):
                raise TypeError(
                    "m_b should contain only integers or floats")
        if len(m_b[0]) != len(b):
            raise ValueError(
                "m_a and m_b can't be multiplied")

        
    result = [[sum(m_a * b for m_a, b in zip(m_a_row, m_b_col))
               for m_b_col in zip(*m_b)]
              for m_a_row in m_a]
    return result
