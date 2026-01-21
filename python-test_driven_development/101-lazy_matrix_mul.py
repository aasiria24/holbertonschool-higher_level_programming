#!/usr/bin/python3
"""
101-lazy_matrix_mul.py
Lazy matrix multiplication using NumPy
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.
    
    Args:
        m_a: First matrix
        m_b: Second matrix
    
    Returns:
        Product of m_a and m_b
    
    Raises:
        TypeError: If inputs are not lists
        ValueError: If matrices cannot be multiplied (numpy error)
    """
    if not isinstance(m_a, list):
        raise TypeError("Scalar operands are not allowed, use '*' instead")
    if not isinstance(m_b, list):
        raise TypeError("Scalar operands are not allowed, use '*' instead")
    
    a = np.array(m_a, dtype=np.float64)
    b = np.array(m_b, dtype=np.float64)
    
    return np.matmul(a, b)


if __name__ == "__main__":
    import sys
    
    def format_output(matrix):
        """Formats numpy matrix output"""
        if isinstance(matrix, np.ndarray):
            rows = []
            for row in matrix:
                elements = [str(int(x)) if x.is_integer() else str(x) for x in row]
                rows.append("[" + " ".join(elements) + "]")
            
            if len(rows) == 1:
                return rows[0]
            return "[" + "\n ".join(rows) + "]"
        return str(matrix)
    
    if len(sys.argv) > 2:
        import ast
        try:
            m_a = ast.literal_eval(sys.argv[1])
            m_b = ast.literal_eval(sys.argv[2])
            result = lazy_matrix_mul(m_a, m_b)
            print(format_output(result))
        except Exception as e:
            print(e)
