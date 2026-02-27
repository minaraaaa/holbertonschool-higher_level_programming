#!/usr/bin/python3
"""
This module provides a custom list class.
"""


class MyList(list):
    """A custom list class that inherits from Python's built-in list."""

    def print_sorted(self):
        """Prints the list in sorted ascending order."""
        print(sorted(self))
