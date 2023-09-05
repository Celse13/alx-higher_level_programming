#!/usr/bin/python3
"""Defines a function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """Divide each element of a matrix by div.
    Args:
        matrix (list): must be a int or a floating value.
        div (int/float): the number for diving each element of a matrix.
    Raises:
        TypeError: When the matrix is not a list or (integers or floats).
        TypeError: when the number of row in matrix are not equal
        TypeError: when the type of div is not int or float.
        ZeroDivisionError: When the value of div is 0.
    Returns:
        New modified matrix where division took place.
    """
    if matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of"
                            "integers/floats")
        if not all((isinstance(val, int) or isinstance(val, float))
                   for val in [num for row in matrix for num in row]):
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")
        if not all(len(row) == len(matrix[0]) for row in matrix):
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
