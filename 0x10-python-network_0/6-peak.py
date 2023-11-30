#!/usr/bin/python3
"""A search for the peak"""


def find_peak(list_of_integers):
    """Find peak"""
    if not list_of_integers:
        return None

    surface = 0
    peak = len(list_of_integers) - 1

    while surface < peak:
        mid = (surface + peak) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            peak = mid
        else:
            surface = mid + 1

    return list_of_integers[surface]
