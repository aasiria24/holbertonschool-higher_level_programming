#!/usr/bin/python3

"""
Module: 2-matrix_divided
Contains function: matrix_divided(matrix, div)
Divides all elements of a matrix by a number
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number
    
    Args:
        matrix: List of lists of integers/floats
        div: Number to divide by (integer or float)
    
    Returns:
        list: New matrix with elements divided by div, rounded to 2 decimal places
    
    Raises:
        TypeError: If matrix is not list of lists of integers/floats,
                   or if rows have different sizes,
                   or if div is not a number
        ZeroDivisionError: If div is zero
    """
    
    # Validate matrix type
    if not isinstance(matrix, list) or \
       not all(isinstance(row, list) for row in matrix) or \
       len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    
    # Validate matrix elements
    for row in matrix:
        if not all(isinstance(num, (int, float)) for num in row):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )
    
    # Validate uniform row size
    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    # Validate div
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    # Create new matrix with divided values
    new_matrix = []
    for row in matrix:
        new_row = []
        for num in row:
            # Divide and round to 2 decimal places
            result = round(num / div, 2)
            new_row.append(result)
        new_matrix.append(new_row)
    
    return new_matrix
