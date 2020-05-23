#!/usr/bin/python3
""" mutiples the matricies!!! """


def matrix_mul(m_a, m_b):
    """ Pythonicallys Doing things without numpy """

    result = [[sum(m_a * b for m_a, b in zip(m_a_row, m_b_col))
               for m_b_col in zip(*m_b)]
              for m_a_row in m_a]
    return result
