#!/usr/bin/env python3
"""
This module demonstrates the use of mixins in Python.
"""


class SwimMixin:
    """A mixin that provides swimming capabilities."""

    def swim(self):
        """Prints the swimming action."""
        print("The creature swims!")


class FlyMixin:
    """A mixin that provides flying capabilities."""

    def fly(self):
        """Prints the flying action."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A Dragon class that inherits capabilities from SwimMixin and FlyMixin.
    """

    def roar(self):
        """Prints the dragon's roar."""
        print("The dragon roars!")
