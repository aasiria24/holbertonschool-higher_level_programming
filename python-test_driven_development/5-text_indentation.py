#!/usr/bin/python3
"""
Module for text_indentation function.
Prints text with 2 new lines after '.', '?', and ':'.
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after '.', '?', and ':'.
    
    Args:
        text: String to be printed with formatting
        
    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    i = 0
    while i < len(text):
        # Skip spaces at the beginning of a line
        if i > 0 and text[i-1] in ".?:" and text[i] == ' ':
            i += 1
            continue
        
        print(text[i], end="")
        
        if text[i] in ".?:":
            print("\n")
        
        i += 1
