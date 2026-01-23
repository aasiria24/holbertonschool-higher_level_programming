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
        TypeError: For type-related errors
    """
    try:
        arr_a = np.array(m_a)
        arr_b = np.array(m_b)
    except Exception as e:
        raise type(e)(str(e))
    
    try:
        result = np.matmul(arr_a, arr_b)
        return result
    except Exception as e:
        raise type(e)(str(e))
