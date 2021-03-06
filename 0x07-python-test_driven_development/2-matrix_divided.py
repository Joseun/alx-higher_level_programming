#!/usr/bin/python3
"""Division of elements in a matrix"""


def matrix_divided(matrix, div):
    """Return a matrix containing the result of the division of elements in a
    matrix.

    Args:
        matrix(:obj:'list'): matrix to be divided
        div(:obj:'int', 'float'): number used to divide the elements


     """
    if not type(div) is int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for lists in matrix:
        for element in lists:
            if not type(element) is int and type(element) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of "
                            "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    new_matrix = [[round(i / div, 2) for i in j] for j in matrix]
    return new_matrix
