#!/usr/bin/python3
"""Inserting a text file."""


def append_after(filename="", search_string="", new_string=""):
    """Inserting a line inside a file."""

    read_line = ""
    with open(filename, 'r') as read_file:
        for current_line in read_file:
            read_line += current_line
            if search_string in current_line:
                read_line += new_string

    with open(filename, 'w') as read_file_2:
        read_file_2.write(read_line)
