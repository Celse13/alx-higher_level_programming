#!/usr/bin/python3
def square_element(x):
    return x ** 2


def square_matrix_simple(matrix=[]):
    sec_matrix = list()

    for element in matrix:
        sec_matrix.append(list(map(square_element, element)))
    return sec_matrix
