#!/usr/bin/python3
"""Implementation of Pascal's Triangle."""


def pascal_triangle(n):
    """Function for Pascal's Triangle Implementation."""

    if n <= 0:
        return []

    tria_representation = [[1]]
    while len(tria_representation) != n:
        last_triangle = tria_representation[-1]
        nex_triangle = [1]
        for i in range(len(last_triangle) - 1):
            nex_triangle.append(last_triangle[i] + last_triangle[i + 1])

        nex_triangle.append(1)
        tria_representation.append(nex_triangle)

    return (tria_representation)
