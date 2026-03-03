#!/usr/bin/python3
"""Class Square that defines a square"""


class Square:
    """Class Square"""

    def __init__(self, size=0):
        """
        Initialize square.
        """
        self.size = size  # Bu, birbaşa setter-i çağırır

    @property
    def size(self):
        """
        Retrieve the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with validation.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns the current square area.
        """
        return self.__size ** 2
