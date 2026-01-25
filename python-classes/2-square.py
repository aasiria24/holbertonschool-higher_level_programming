#!/usr/bin/python3
"""
Module: 2-square
This module defines a square class with validated size attribute.
"""


class Square:
    """
    This class defines a square using a private instance attribute.
    It ensures that the size provided is always a valid non-negative integer.
    """

    def __init__(self, size=0):
        """
        Initalizes a new Square instance with validation.

        The size of the square must be an integer greater than or equal to zero.
        Otherwise, an appropriate exception will be raised.

        Args:
        size (int, optional): The size of the square. Defaults to 0.

        Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size size must be >= 0")

        self.__size = size
