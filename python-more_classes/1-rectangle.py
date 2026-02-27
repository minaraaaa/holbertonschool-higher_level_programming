#!/usr/bin/python3
"""
This module defines a Rectangle class with private attributes.
"""


class Rectangle:
    """Representation of a rectangle."""

    def __init__(self, width=0, height=0):
        """Initializes the rectangle with optional width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for the private instance attribute __width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the private instance attribute __width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the private instance attribute __height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the private instance attribute __height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
