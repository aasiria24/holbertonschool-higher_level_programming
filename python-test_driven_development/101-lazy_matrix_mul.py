#!/usr/bin/python3
"""
Module for lazy_matrix_mul function.
Multiplies two matrices using NumPy.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a: First matrix (list of lists of integers or floats)
        m_b: Second matrix (list of lists of integers or floats)

    Returns:
        Result of matrix multiplication as a numpy array

    Raises:
        ValueError: For various input validation errors
    """
    return np.matmul(m_a, m_b)
