#!/usr/bin/python3
"""Dynamic importation of BaseGeometry Class."""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Representation of Rectangle."""

    def __init__(self, width, height):
        """Constructor for Rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
