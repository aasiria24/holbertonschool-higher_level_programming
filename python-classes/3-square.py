#!/usr/bin/python3
"""
This module defines a Square class with area calculation.
The class validates the size value and can compute the square area.
"""


class Square:
    """
    This class represent a square shape.

    It store the size of the square as a private instance attribute
    and provides a public method to calculate the area of the square.
    """
    
    def __init__(self, size=0):
        """
        Initializes a new Square instance with validation.
        
        The size must be an integer greater than or equal to zero.
        if the value provided is invalid, an exception is raised.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
    
    def area(self):
        """
        Calculates and returns the area of the square.
        
        Returns:
            int: The area of the square (size * size).
        """
        return self.__size ** 2
