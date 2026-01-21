#!/usr/bin/python3
"""
Module: 5-text_indentation

Contains function: text_indentation(text)
Prints a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    chars = ".?:"
    i = 0

    while i < len(text):
        print(text[i], end="")
        if text[i] in chars:
            print()
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1

    if text == "":
        print()
