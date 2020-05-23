#!/usr/bin/python3
import numpy as np
""" easy matrix multiplication! """


def lazy_matrix_mul(m_a, m_b):
    """ NP WINS!!! Mathtality """

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
    a = np.array(m_a)
    b = np.array(m_b)
    return a.dot(b)
