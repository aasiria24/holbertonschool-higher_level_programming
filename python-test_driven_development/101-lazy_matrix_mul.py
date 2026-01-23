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
        m_a: First matrix (list of lists of integers or floats)
        m_b: Second matrix (list of lists of integers or floats)

    Returns:
        Result of matrix multiplication as a numpy array

    Raises:
        ValueError: For various input validation errors
        TypeError: For type-related errors
    """
  if not isinstance(m_a, list):
        raise ValueError("Scalar operands are not allowed, use '*' instead")
    if not isinstance(m_b, list):
        raise ValueError("Scalar operands are not allowed, use '*' instead")

    if len(m_a) == 0:
        if len(m_b) == 0:
            raise ValueError("shapes (0,) and (0,) not aligned: 0 (dim 0) != 0 (dim 0)")
        arr_b = np.array(m_b)
        shape_str = str(arr_b.shape).replace(" ", "")
        raise ValueError(f"shapes (0,) and {shape_str} not aligned: 0 (dim 0) != {arr_b.shape[0]} (dim 0)")

    if len(m_b) == 0:
        arr_a = np.array(m_a)
        shape_str = str(arr_a.shape).replace(" ", "")
        raise ValueError(f"shapes {shape_str} and (0,) not aligned: {arr_a.shape[-1]} (dim 1) != 0 (dim 0)")

    if isinstance(m_a[0], list) and len(m_a[0]) == 0:
        if isinstance(m_b[0], list) and len(m_b[0]) == 0:
            raise ValueError("shapes (1,0) and (1,0) not aligned: 0 (dim 1) != 1 (dim 0)")
        arr_b = np.array(m_b)
        shape_str = str(arr_b.shape).replace(" ", "")
        raise ValueError(f"shapes (1,0) and {shape_str} not aligned: 0 (dim 1) != {arr_b.shape[0]} (dim 0)")

    if isinstance(m_b[0], list) and len(m_b[0]) == 0:
        arr_a = np.array(m_a)
        shape_str = str(arr_a.shape).replace(" ", "")
        raise ValueError(f"shapes {shape_str} and (1,0) not aligned: {arr_a.shape[-1]} (dim 1) != 1 (dim 0)")

    arr_a = np.array(m_a)
    arr_b = np.array(m_b)

    if arr_a.ndim < 2:
        arr_a = arr_a.reshape(1, -1) if arr_a.ndim == 1 else arr_a.reshape(1, 1)
    if arr_b.ndim < 2:
        arr_b = arr_b.reshape(-1, 1) if arr_b.ndim == 1 else arr_b.reshape(1, 1)

    if arr_a.shape[-1] != arr_b.shape[0]:
        shape_a_str = str(arr_a.shape).replace(" ", "")
        shape_b_str = str(arr_b.shape).replace(" ", "")
        raise ValueError(f"shapes {shape_a_str} and {shape_b_str} not aligned: {arr_a.shape[-1]} (dim 1) != {arr_b.shape[0]} (dim 0)")

    return np.matmul(arr_a, arr_b)
