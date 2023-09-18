#!/usr/bin/python3
"""Import the class of Rectangle."""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Representation of the class of square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor for Square class."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Retrieving the size of the side of square."""
        return (self.width)

    @size.setter
    def size(self, value):
        """Setting the value for the sides of a square."""
        self.integer_validator('width', value)
        self.width = value
        self.integer_validator('height', value)
        self.height = value

    def __str__(self):
        """module string represation of square
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.width)

    def update(self, *args, **kwargs):
        """Dealing with extra positional arguments and keyworded arguments."""
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
        """Returning the dictionary representation of the square."""
        return {
            "id": self.id,
            "x": self.x,
            "size": self.size,
            "y": self.y
        }
