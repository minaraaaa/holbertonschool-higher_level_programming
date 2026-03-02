#!/usr/bin/python3
"""
This module provides a function for text indentation.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :
    No space at the beginning or at the end of each printed line.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special_chars = [".", "?", ":"]
    i = 0
    text = text.strip()

    while i < len(text):
        print(text[i], end="")
        if text[i] in special_chars:
            print("\n")
            i += 1
            # Növbəti sətirin əvvəlindəki boşluqları atlayırıq
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
