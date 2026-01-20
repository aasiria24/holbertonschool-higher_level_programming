#!/usr/bin/python3

"""
Module: 0-add_integer
Contains function: add_integer(a, b=98)
Adds two integers and returns the result
"""


def add_integer(a, b=98):
    """
    Adds two integers
    
    Args:
        a: First number (int or float)
        b: Second number (int or float), defaults to 98
    
    Returns:
        int: Sum of a and b as integer
    
    Raises:
        TypeError: If a or b are not integers or floats
    """
    
    # Check if a is integer or float
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    
    # Check if b is integer or float
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    # Cast to integers if they are floats
    a = int(a) if isinstance(a, float) else a
    b = int(b) if isinstance(b, float) else b
    
    # Return the addition as integer
    return a + b
