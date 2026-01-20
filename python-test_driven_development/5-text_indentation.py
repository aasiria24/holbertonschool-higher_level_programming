#!/usr/bin/python3
"""
Module: 5-text_indentation

Contains function: text_indentation(text)
Prints a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """Prints text with 2 new lines after each ., ? and :
    Args:
        text: The text to process (must be a string)
    Returns:
        None
    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    length = len(text)

    while i < length:
        print(text[i], end='')

        if text[i] in ".?:":

            if i != length - 1:
                print("\n")

                i += 1
                while i < length and text[i] == ' ':
                    i += 1
                    continue

                i += 1
