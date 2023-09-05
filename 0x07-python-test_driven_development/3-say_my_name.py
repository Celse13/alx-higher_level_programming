#!/usr/bin/python3
"""Defines a function that prints the full_name of the user."""


def say_my_name(first_name, last_name=""):
    """Print a full name.
    Args:
        first_name (str): first name to be displayed
        last_name (str): last name to be displayed
    Raises:
        TypeError: When first_name and last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
