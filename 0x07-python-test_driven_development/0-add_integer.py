#!/usr/bin/python3
"""Defines a function that should add two integers.
Performs mathematical calculation
Returs the additiona of two numbers on successful
"""


def add_integer(a, b=98):
    """Adding two integers a and b.
    Floats are first treated like int before adding them
    Raises:
    TypeError: If a and b are not integers or floats
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
