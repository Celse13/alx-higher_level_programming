#!/usr/bin/python3
"""Dynamic importation of Rectangle Class."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Representation of Square."""
    def __init__(self, size):
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size
