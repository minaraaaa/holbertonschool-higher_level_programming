#!/usr/bin/python3
"""
This module provides a function that formats and prints text.
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after each '.', '?', and ':'.
    Removes leading and trailing spaces from each printed line.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    s = text.replace('.', '.\n\n').replace('?', '?\n\n').replace(':', ':\n\n')

    lines = [line.strip(' \t') for line in s.split('\n')]

    print("\n".join(lines), end="")
