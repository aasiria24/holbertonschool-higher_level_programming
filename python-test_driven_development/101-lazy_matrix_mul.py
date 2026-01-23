#!/usr/bin/python3
"""
Module: 101-lazy_matrix_mul
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy
    """
    if not isinstance(m_a, list):
        raise TypeError
    if not isinstance(m_b, list):
        raise TypeError

    if m_a == [] or m_a == [[]]:
        raise ValueError
    if m_b == [] or m_b == [[]]:
        raise ValueError

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError

    if not all(all(isinstance(el, (int, float)) for el in row) for row in m_a):
        raise TypeError
    if not all(all(isinstance(el, (int, float)) for el in row) for row in m_b):
        raise TypeError

    row_len_a = len(m_a[0])
    if not all(len(row) == row_len_a for row in m_a):
        raise TypeError

    row_len_b = len(m_b[0])
    if not all(len(row) == row_len_b for row in m_b):
        raise TypeError

    if row_len_a != len(m_b):
        raise ValueError

    return np.matmul(m_a, m_b)
