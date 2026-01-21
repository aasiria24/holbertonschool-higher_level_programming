#!/usr/bin/python3
"""
101-lazy_matrix_mul.py
Simple solution that returns formatted string
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices and returns formatted string.
    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("Scalar operands are not allowed, use '*' instead")
    
    a = np.array(m_a, dtype=np.float64)
    b = np.array(m_b, dtype=np.float64)
    
    result = np.matmul(a, b)
    
    return format_numpy_matrix(result)


def format_numpy_matrix(mat):
    """
    Format numpy matrix to remove decimal points for integers.
    """
    if mat.ndim == 1:
        formatted = [str(int(x)) if x.is_integer() else str(x) for x in mat]
        return "[" + " ".join(formatted) + "]"
    
    lines = []
    for i, row in enumerate(mat):
        formatted_row = [str(int(x)) if x.is_integer() else str(x) for x in row]
        row_str = "[" + " ".join(formatted_row) + "]"
        
        if i == 0:
            lines.append(row_str)
        else:
            lines.append(" " + row_str)
    
    return "[" + "\n".join(lines) + "]"
