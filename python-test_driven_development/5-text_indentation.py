#!/usr/bin/python3
"""
This module provides a function that formats and prints text.
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after each '.', '?', and ':'.
    Removes leading and trailing spaces from each printed line.

    Args:
        text (str): The text to be formatted.

    Raises:
        TypeError: If text is not a string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    # Xüsusi simvollardan sonra 2 yeni sətir əlavə edirik
    s = text.replace('.', '.\n\n').replace('?', '?\n\n').replace(':', ':\n\n')
    
    # Mətni sətirlərə bölüb, hər sətrin əvvəlindən və sonundan boşluqları silirik
    lines = [line.strip(' \t') for line in s.split('\n')]
    
    # Sətirləri yenidən birləşdirib ekrana çap edirik (sonda əlavə boşluq olmadan)
    print("\n".join(lines), end="")
