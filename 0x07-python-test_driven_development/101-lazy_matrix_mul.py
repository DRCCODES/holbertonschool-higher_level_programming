#!/usr/bin/python3
import numpy as np
""" easy matrix multiplication! """


def lazy_matrix_mul(m_a, m_b):
    """ NP WINS!!! Mathtality """
    a = np.array(m_a)
    b = np.array(m_b)
    return a.dot(b)
