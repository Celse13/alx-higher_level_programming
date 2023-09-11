#!/usr/bin/python3
"""Checking whether an object is an instance of a class."""


def is_kind_of_class(obj, a_class):
    """Checking if obj is an instance of a_class.
    Args:
        obj: an object of class
        a_class: a class
    Returns:
        True if obj is a instance of a_class
    """
    if isinstance(obj, a_class):
        return (True)
    return (False)
