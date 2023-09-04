#!/usr/bin/python3
"""Definition of MagicClass that works as bytecodes."""

import math


class MagicClass:
    """Representation of the class of a circle."""

    def __init__(self, radius=0):
        """Constructr for the new instances.
        Arg:
            radius (float or int): radius for new instances.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return The area of new instance."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return circumference of new instance."""
        return (2 * math.pi * self.__radius)
