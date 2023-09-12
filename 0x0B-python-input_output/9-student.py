#!/usr/bin/python3
"""Student class."""


class Student:
    """Representation of the student."""

    def __init__(self, first_name, last_name, age):
        """Constructor for the student."""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Dictionary description with simple data."""
        return (self.__dict__)
