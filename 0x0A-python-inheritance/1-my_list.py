#!/usr/bin/python3
"""Inherint from the class of list."""


class MyList(list):
    """Represt a class for handling built in sorted print func."""

    def print_sorted(self):
        """Print the element of list in ascending order."""
        print(sorted(self))
