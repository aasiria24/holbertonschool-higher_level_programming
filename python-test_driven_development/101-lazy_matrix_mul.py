#!/usr/bin/python3
# Amaal Asiri <github: aasiria24>
"""
Module for lazy_matrix_mul function.
Multiplies two matrices using NumPy.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
    m_a (list of lists): First matrix
    m_b (list of lists): Second matrix

    Returns:
    A new matrix which is the result of the multiplication

    Raises:
    TypeError: if matrices are not lists of lists of integers/floats
    ValueError: if matrices are empty or cannot be multiplied
    """
    try:
        return np.matmul(m_a, m_b)
    except ValueError as e:
        raise ValueError(str(e))
    except TypeError as e:
        raise TypeError(str(e))
