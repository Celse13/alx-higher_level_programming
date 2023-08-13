#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for elements in matrix:
        for element in elements:
            print("{:d}".format(element), end=" ")
        print("")
