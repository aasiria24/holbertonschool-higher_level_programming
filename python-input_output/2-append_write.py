#!/usr/bin/python3
"""
Module for appending a string to text file.
"""


def append_write(filename="", text=""):
    """
    Write a function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added.

    Args:
    filename (str): The name of file to add characters to.
    chracters (str): The character to add to the file.

    Returns:
    int: The number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)
        return len(text)
