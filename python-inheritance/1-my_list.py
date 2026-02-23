#!/usr/bin/python3
"""Module 1-my_list: defines MyList class with print_sorted method"""


class MyList(list):
    """MyList inherits from list and adds a print_sorted method"""

    def print_sorted(self):
        """Prints the list in ascending order without modifying the original"""
        print(sorted(self))
