#!/usr/bin/python3
"""
Module for lazy matrix multiplication using NumPy
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.
    
    Returns:
        The product matrix as a NumPy array
    """
    # Basic validation
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("Scalar operands are not allowed, use '*' instead")
    
    # Convert to numpy arrays
    try:
        a = np.array(m_a, dtype=float)
        b = np.array(m_b, dtype=float)
    except:
        raise ValueError("m_a and m_b must contain only numbers")
    
    # Check dimensions
    if a.ndim != 2 or b.ndim != 2:
        raise ValueError("Both arguments must be 2D matrices")
    
    if a.shape[1] != b.shape[0]:
        raise ValueError("m_a and m_b can't be multiplied")
    
    # Multiply
    result = np.dot(a, b)
    
    # Convert integers back to int type if possible
    if np.all(np.equal(np.mod(result, 1), 0)):
        result = result.astype(int)
    
    return result


def print_numpy_matrix(matrix):
    """
    Prints numpy matrix in the required format.
    """
    if matrix.ndim == 1:
        # 1D array
        print("[" + " ".join(str(int(x) if x.is_integer() else x) for x in matrix) + "]")
    else:
        # 2D array
        rows = []
        for row in matrix:
            elements = []
            for x in row:
                # Check if integer (handle both numpy and python types)
                if hasattr(x, 'is_integer') and x.is_integer():
                    elements.append(str(int(x)))
                elif isinstance(x, (int, np.integer)):
                    elements.append(str(x))
                else:
                    elements.append(str(x))
            rows.append("[" + " ".join(elements) + "]")
        print("[" + "\n ".join(rows) + "]")


# اختبار مباشر
if __name__ == "__main__":
    # Example from the test
    m_a = [[1, 2], [3, 4]]
    m_b = [[5, 6], [7, 8]]
    
    result = lazy_matrix_mul(m_a, m_b)
    print_numpy_matrix(result)
