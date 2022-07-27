#!/usr/bin/python3
"""implements a function -> def matrix() that
 divides all elements of a matrix"""


def matrix_divided(matrix, div):
    new_matrix, new_row = [], []
    prev_len = 0
    messages = (
        'matrix must be a matrix (list of lists) of integers/floats',
        'Each row of the matrix must have the same size',
        'div must be a number',
        'division by zero'
    )
    if type(matrix) is not list or matrix == []:
        raise TypeError(messages[0])

    for row in matrix:
        if type(row) is not list or row == []:
            raise TypeError(messages[0])
        for item in row:
            if type(item) not in [int, float]:
                raise TypeError(messages[0])

        current_len = len(row)
        if current_len != prev_len and prev_len != 0:
            raise TypeError(messages[1])
        prev_len = current_len

    if type(div) not in [int, float]:
        raise TypeError(messages[2])
    if div == 0:
        raise ZeroDivisionError(messages[3])
    for row in matrix:
        new_row = list(map(lambda x: round(x / div, 2), row))
        new_matrix.append(new_row)
    return new_matrix
