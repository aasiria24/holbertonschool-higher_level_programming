#!/usr/bin/python3
"""
Module: 5-text_indentation
Prints a text with a new line after each of these characters: ., ? and :
"""


def text_indentation(text):
    """Prints text with new line after each ., ? and :"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    length = len(text)

    while i < length:
        if text[i] in ".?:":
            print(text[i], end="\n")  # العلامة + newline
            i += 1
            while i < length and text[i] == " ":
                i += 1
            continue
        else:
            print(text[i], end="")  # باقي الحروف بدون newline
        i += 1

    # ← تأكد من أن النص النهائي يحتوي على newline
    print("", end="")

