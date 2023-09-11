#!/usr/bin/python3
"""Definition of the BaseGeometry class."""


class BaseGeometry:
    """Representation of BaseGeometry."""

    def area(self):
        """Implementation for calculating the area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validation for the integer.
        Args:
            name (string): string input
            valued (int) : int input
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
