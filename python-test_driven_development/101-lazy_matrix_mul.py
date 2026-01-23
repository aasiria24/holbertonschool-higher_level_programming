#!/usr/bin/python3
# Amaal Asiri <github: aasiria24>
"""
Module for lazy_matrix_mul function.
Multiplies two matrices using NumPy.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices using NumPy.

    Args:
        m_a: First matrix
        m_b: Second matrix

    Returns:
        Result of matrix multiplication
    """
    return np.matmul(m_a, m_b)
