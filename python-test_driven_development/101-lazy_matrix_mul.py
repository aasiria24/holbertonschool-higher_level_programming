#!/usr/bin/python3
"""
Module for lazy matrix multiplication using NumPy
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.
    """
    # Check if inputs are lists
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("Scalar operands are not allowed, use '*' instead")
    
    # Check if lists are empty
    if not m_a or not m_b:
        raise ValueError("m_a and m_b can't be empty")
    
    # Check if all elements are lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    
    # Check if all elements are numbers
    for row in m_a:
        if not all(isinstance(x, (int, float)) for x in row):
            raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        if not all(isinstance(x, (int, float)) for x in row):
            raise TypeError("m_b should contain only integers or floats")
    
    # Convert to numpy arrays
    try:
        a = np.array(m_a, dtype=np.float64)
        b = np.array(m_b, dtype=np.float64)
    except:
        raise TypeError("m_a and m_b must be lists of lists containing numbers")
    
    # Perform matrix multiplication
    try:
        result = np.matmul(a, b)
    except ValueError as e:
        raise ValueError("m_a and m_b can't be multiplied") from e
    
    return result
