#!/usr/bin/env python3
"""
This module defines a VerboseList class that extends the built-in list
to print notifications upon modification.
"""


class VerboseList(list):
    """A custom list class that prints notifications when modified."""

    def append(self, item):
        """Adds an item to the list and prints a notification."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, x):
        """Extends the list and prints a notification with the count."""
        count = len(x)
        super().extend(x)
        print("Extended the list with [{}] items.".format(count))

    def remove(self, item):
        """Removes an item from the list and prints a notification."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Pops an item from the list and prints a notification."""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
