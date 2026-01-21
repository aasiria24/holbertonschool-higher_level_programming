#!/usr/bin/python3
"""
Module for text indentation
"""


def text_indentation(text):
    """Prints text with 2 new lines after . ? :"""
    if type(text) is not str:
        raise TypeError("text must be a string")

    text = text.strip()

    if text == "":
        return

    if text in ['.', '?', ':']:
        return 

    i = 0
    while i < len(text):
        if text[i] in ['.', '?', ':']:
            print(text[i] + '\n')
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
        else:
            print(text[i], end='')
            i += 1
