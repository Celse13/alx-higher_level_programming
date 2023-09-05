#!/usr/bin/python3
"""Definition of a locked class."""


class LockedClass:
    """Preventing the user from creating any attributes.
        except 'first_name'
    """

    __slots__ = ["first_name"]
