#!/usr/bin/python3
"""Inherint from the class of list."""


class MyList(list):
    """Inherint from the class of list."""

    def print_sorted(self):
        """Print the element of list in ascending order."""
        sorted_list = sorted(self)
        return (sorted_list)
