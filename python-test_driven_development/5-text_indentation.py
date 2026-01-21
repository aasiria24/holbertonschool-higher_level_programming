#!/usr/bin/python3
"""
Module for text indentation
This module provides a function to print text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after each '.', '?', and ':'

    Args:
        text (str): The text to format and print

        Raises:
        TypeError: If text is not a string

        Examples:
        >>> text_indentation("Hello. How are you? I'm fine: thank you.")
        Hello.
        <BLANKLINE>
        How are you?
        <BLANKLINE>
        I'm fine:
        <BLANKLINE>
        thank you.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special_chars = ['.', '?', ':']

    i = 0
    length = len(text)

    while i < length:
        print(text[i], end='')

        if text[i] in special_chars:
            print('\n')

            i += 1
            while i < length and text[i] == ' ':
                i += 1
            continue

        i += 1
