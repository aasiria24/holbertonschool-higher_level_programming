#!/usr/bin/python3
"""
Text Indentation Module

This module provides a function that prints a text with 2 new lines
after '.', '?' and ':'.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after '.', '?' and ':'.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip()
    if text == "":
        return

    i = 0
    n = len(text)

    while i < n:
        ch = text[i]

        print(ch, end="")

        if ch in ".?:":
            j = i + 1
            while j < n and text[j] == ch:
                print(text[j], end="")
                j += 1

            print("\n")

            while j < n and text[j] in " \t\n":
                j += 1

            i = j
            continue

        i += 1
