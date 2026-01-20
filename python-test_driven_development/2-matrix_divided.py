#!/usr/bin/python3
"""Module that provides a function to divide all elements of a matrix."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div.

    Raises:
        TypeError: If matrix is invalid or div is not a number.
        ZeroDivisionError: If div is 0.
    """
    # Check matrix type and non-empty rows
    if (not isinstance(matrix, list) or not matrix or
        any(not isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check all elements are int or float
    for row in matrix:
        if not all(isinstance(el, (int, float)) for el in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check all rows have same size
    row_lengths = [len(row) for row in matrix]
    if len(set(row_lengths)) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Check div
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Return new matrix with divided elements rounded to 2 decimals
    return [[round(el / div, 2) for el in row] for row in matrix]

