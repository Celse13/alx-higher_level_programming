#!/usr/bin/python3
"""Importing Base Class from the ___init__ package."""


from models.base import Base


class Rectangle(Base):
    """The class of Rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializer for the Rectangle class."""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Retrieving the value of width."""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Setting the value of width."""
        self.integer_validator('width', value)
        self.__width = value

    @property
    def height(self):
        """Retrieving the value of height."""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Setting the value of height."""
        self.integer_validator('height', value)
        self.__height = value

    @property
    def x(self):
        """Retrieving the value of x."""
        return (self.__x)

    @x.setter
    def x(self, value):
        """Setting the value of x."""
        self.integer_validator('x', value)
        self.__x = value

    @property
    def y(self):
        """Retrieving the value of y."""
        return (self.__y)

    @y.setter
    def y(self, value):
        """Setting the value of y."""
        self.integer_validator('y', value)
        self.__y = value

    def area(self):
        """"Calculate the area of a rectangle."""
        return (self.height * self.width)

    def integer_validator(self, instance_var, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(instance_var))
        if instance_var == "x" or instance_var == "y":
            if value < 0:
                raise ValueError("{} must be >= 0".format(instance_var))
        elif value <= 0:
            raise ValueError("{} must be > 0".format(instance_var))

    def display(self):
        """"Printing Rectangle instance with the character # at stdout."""
        display_rectangle = ""
        print("\n" * self.y, end='')
        for i in range(self.height):
            display_rectangle += (" " * self.x) + ("#" * self.width) + "\n"
        print(display_rectangle, end='')

    def __str__(self):
        """Readable rectangle representation."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """Dealing with extra positional arguments and key value pairs."""
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        """Returning the dictionary representation of the rectangle."""
        return {'x': getattr(self, "x"),
                'y': getattr(self, "y"),
                'id': getattr(self, "id"),
                'height': getattr(self, "height"),
                'width': getattr(self, "width")}
