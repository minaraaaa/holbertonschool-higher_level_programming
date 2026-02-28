#!/usr/bin/env python3
"""
This module defines an abstract base class Animal and its subclasses.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class representing an Animal."""

    @abstractmethod
    def sound(self):
        """Abstract method representing the animal's sound."""
        pass


class Dog(Animal):
    """Subclass representing a Dog."""

    def sound(self):
        """Returns the dog's sound."""
        return "Bark"


class Cat(Animal):
    """Subclass representing a Cat."""

    def sound(self):
        """Returns the cat's sound."""
        return "Meow"
