#!/usr/bin/python3
"""Representation for the class of square"""


from inspect import classify_class_attrs
from models.rectangle import Rectangle


class Square(Rectangle):
    """Definition of the square.

     Attributes:
        width (int): width instance width.
        height (int): height instance width.
        x (int): x instance size.
        y (int): y instance size.
        id (int): Id for each square instance.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the new square instance

        Args:
            size (int): size for the sides of the square.
            x (int): The value of the size of x
            y (int): The value of the size of y.
            id (int): The value of the id of square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Display the square."""
        return ("[Square] ({}) {:d}/{:d} - {:d}".
                format(self.id, self.x, self.y, self.size))

    @property
    def size(self):
        """Retrieving the value of size.

        Returns:
            int: size of the sides of a square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """Setting the valueo of the size.
        Args:
            value (int): size for the sides of a square.
        Raises:
            TypeError: When the width is not an instance of int.
            ValueError: When width < 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Handling the extra arguments and key/value pairs

        Args:
            *args (tuple): extra positional arguments.
            **kwargs (dict): extra key/value pairs.
        """
        if args and len(args) != 0:
            for idx, arg in enumerate(args):
                if idx == 0:
                    self.id = arg
                elif idx == 1:
                    self.size = arg
                elif idx == 2:
                    self.x = arg
                elif idx == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Make dict for the square.

        Returns:
            dict: dict representation of the square.
        """
        return {
            "id": self.id,
            "x": self.x,
            "size": self.size,
            "y": self.y
        }
