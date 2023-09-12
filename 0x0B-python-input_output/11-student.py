#!/usr/bin/python3
"""Student class."""


class Student:
    """Representation of the student."""

    def __init__(self, first_name, last_name, age):
        """Constructor for the student."""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Dictionary description with simple data."""

        if (type(attrs) == list and
                all(type(val) == str for val in attrs)):
            return {u: getattr(self, u) for u in attrs if hasattr(self, u)}
        return (self.__dict__)

    def reload_from_json(self, json):
        """Reloading an object from json."""

        for idx, val in json.items():
            setattr(self, idx, val)
