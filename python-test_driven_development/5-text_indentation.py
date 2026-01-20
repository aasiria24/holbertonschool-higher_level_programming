#!/usr/bin/python3
"""
Module: 5-text_indentation

Contains function: text_indentation(text)
Prints a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """Prints a text with 2 new lines after each ., ? and :
    Args:
        text: The text to process (must be a string)

    Returns:
        None

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = ".?:"
     start = 0

    for i, char in enumerate(text):
        if char in separators:
            line = text[start:i + 1].strip()
            if line:
                print(line)
                start = i + 1

                remaining = text[start:].strip()
                if remaining:
                    print(remaining)
