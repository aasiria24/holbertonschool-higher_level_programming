#!/usr/bin/python3
"""Module 2-matrix_divided: Provides a function to divide all elements of a matrix."""

def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div and return a new matrix.

    Each element is rounded to 2 decimal places.
    Raises TypeError if matrix is not a list of lists of integers/floats
    or if rows are of different sizes. Raises TypeError if div is not a number.
    Raises ZeroDivisionError if div is 0.
    """
    if (not isinstance(matrix, list) or not matrix or
            any(not isinstance(row, list) for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    for row in matrix:
        if not all(isinstance(el, (int, float)) for el in row):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )

    row_lengths = [len(row) for row in matrix]
    if len(set(row_lengths)) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(el / div, 2) for el in row] for row in matrix]
