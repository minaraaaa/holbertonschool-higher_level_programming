#!/usr/bin/env python3
"""
This module provides a CountedIterator class that extends the built-in
iterator to keep track of the number of iterated items.
"""


class CountedIterator:
    """An iterator that counts how many items have been fetched."""

    def __init__(self, some_iterable):
        """
        Initializes the iterator object and the counter.
        """
        self.iterator = iter(some_iterable)
        self.counter = 0

    def get_count(self):
        """
        Returns the current value of the counter.
        """
        return self.counter

    def __next__(self):
        """
        Fetches the next item from the iterator and increments the counter.
        Raises StopIteration when no items are left.
        """
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration
