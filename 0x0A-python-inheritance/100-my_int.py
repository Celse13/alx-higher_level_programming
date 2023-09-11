#!/usr/bin/python3
"""Definitation of a class of MyInt that inherits from int."""


class MyInt(int):
    """Represenation of MyInt"""

    def __eq__(self, value):
        """Changing the behaviour of == to !=."""
        return (self.real != value)

    def __ne__(self, value):
        """Changing the behavior of != to ==."""
        return (self.real == value)
