#!/usr/bin/python3
"""
Module: 5-text_indentation

Contains function: text_indentation(text)
Prints a text with a new line after each ., ? and :
"""

def text_indentation(text):
    """Prints text with a new line after each ., ? and :"""

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
