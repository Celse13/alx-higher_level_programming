#!/usr/bin/python3
"""Defines a function that prints the square of #."""


def print_square(size):
    """Print a square of the # to form a square.
    Args:
        size (int): the size of the square.
    Raises:
        TypeError: When the size is not integer.
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
