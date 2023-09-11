#!/usr/bin/python3
"""Implementation of function that adds attributes to object."""


def add_attribute(obj, att, value):
    """Adding attributes to obj."""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
