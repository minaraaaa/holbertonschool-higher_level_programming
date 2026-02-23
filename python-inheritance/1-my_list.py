#!/usr/bin/python3
"""Module 1-my_list: defines MyList class"""

class MyList(list):
    """MyList inherits from list and has a print_sorted method"""
    def print_sorted(self):
        """Prints the list in ascending order without modifying original"""
        print(sorted(self))
