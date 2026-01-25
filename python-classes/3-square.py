#!/usr/bin/python3
"""
Module: 3-square
This module defines a Square class with area calculation.
"""


class Square:
    """
    A class that defines a square with validation and area calculation.
    
    Attributes:
        __size (int): The size of the square (private attribute).
    """
    
    def __init__(self, size=0):
        """
        Initializes a new Square instance with validation.
        
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
