#!/usr/bin/env python3
"""
This module defines a Shape abstract class and concrete shapes,
demonstrating duck typing in Python.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class representing a geometric shape."""

    @abstractmethod
    def area(self):
        """Abstract method to calculate the area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method to calculate the perimeter."""
        pass


class Circle(Shape):
    """A Circle shape."""

    def __init__(self, radius):
        """Initializes the circle with a radius."""
        self.radius = radius

    def area(self):
        """Returns the calculated area of the circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Returns the calculated perimeter of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """A Rectangle shape."""

    def __init__(self, width, height):
        """Initializes the rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Returns the calculated area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Returns the calculated perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints the area and perimeter of a shape.
    Relying on duck typing, it assumes the shape has area() and perimeter().
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
