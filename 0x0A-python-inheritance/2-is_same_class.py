#!/usr/bin/python3
"""Checking whether an object is an instance of a class."""


def is_same_class(obj, a_class):
    """Checking if obj is an instance of a_class."""
    if isinstance(obj, a_class):
        return (True)
    else:
        return (False)
