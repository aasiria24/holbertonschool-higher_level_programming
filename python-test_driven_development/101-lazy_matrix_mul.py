#!/usr/bin/python3
"""
Module for lazy matrix multiplication using NumPy
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.
    """
    a = np.array(m_a)
    b = np.array(m_b)
    
    result = np.matmul(a, b)
    
    if np.all(result == result.astype(int)):
        result = result.astype(int)
    
    return result
