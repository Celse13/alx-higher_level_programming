#!/usr/bin/python3
"""Define a class for rectangle."""


class Rectangle:
    """Representation of a rectangle."""

    def __init__(self, width=0, height=0):
        """Constructing new object with attributes.
        Args:
        width (int): width for the new instance.
        height (int): height for the new instance.
        """
        self.width = width
        self.height = height

        @property
        def width(self):
            """Retrieving the provided width."""
            return (self.__width)

        @width.setter
        def width(self, value):
            """Setting the width with new value.
            Args:
            value (int): new value for width
            Returns:
            New width
            """
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

            @property
            def height(self):
                """Retrieving the provided height."""
                return (self.__height)

            @height.setter
            def height(self, value):
                """Setting the width with new value.
                Args:
                value (int): new value for height
                Returns:
                New height
                """
                if not isinstance(value, int):
                    raise TypeError("height must be an integer")
                if value < 0:
                    raise ValueError("height must be >= 0")
                self.__height = value
