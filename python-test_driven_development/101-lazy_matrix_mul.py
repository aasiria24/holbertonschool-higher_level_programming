#!/usr/bin/python3
"""
Module for lazy matrix multiplication using NumPy
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.
    
    Args:
        m_a: First matrix (list of lists of ints/floats)
        m_b: Second matrix (list of lists of ints/floats)
    
    Returns:
        Product of the two matrices as a NumPy array
    
    Raises:
        TypeError: If matrices are not lists of lists
        ValueError: If matrices cannot be multiplied
    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("Scalar operands are not allowed, use '*' instead")
    
    try:
        a = np.array(m_a, dtype=float)
        b = np.array(m_b, dtype=float)
    except (ValueError, TypeError):
        raise TypeError("m_a and m_b must be lists of lists containing numbers")
    
    try:
        result = np.matmul(a, b)
    except ValueError as e:
        raise ValueError(str(e))
    
    return result


def print_matrix(matrix):
    """
    Prints matrix in the required format without decimal points for integers.
    """
    if isinstance(matrix, np.ndarray):
        rows = []
        for row in matrix:
            elements = []
            for elem in row:
                if isinstance(elem, (int, np.integer)) or (isinstance(elem, float) and elem.is_integer()):
                    elements.append(str(int(elem)))
                else:
                    elements.append(str(elem))
            rows.append("[" + " ".join(elements) + "]")
        
        if len(rows) == 1:
            print(rows[0])
        else:
            print("[" + "\n ".join(rows) + "]")
    else:
        print(matrix)


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 2:
        try:
            import ast
            m_a = ast.literal_eval(sys.argv[1])
            m_b = ast.literal_eval(sys.argv[2])
            
            result = lazy_matrix_mul(m_a, m_b)
            print_matrix(result)
        except Exception as e:
            print(e)
    else:
        test_cases = [
            ([[1, 2], [3, 4]], [[5, 6], [7, 8]]),
            ([[]], [[1, 2], [3, 4]]),
            ([[1, 2]], [[3, 4], [5, 6]]),
        ]
        
        for i, (m_a, m_b) in enumerate(test_cases):
            print(f"\nTest case {i+1}:")
            print(f"m_a = {m_a}")
            print(f"m_b = {m_b}")
            try:
                result = lazy_matrix_mul(m_a, m_b)
                print_matrix(result)
            except Exception as e:
                print(f"Error: {e}")
