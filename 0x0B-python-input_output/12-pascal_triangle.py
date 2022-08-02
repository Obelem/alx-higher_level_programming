#!/usr/bin/python3
"""Defines a function that generates pascal's triangle"""


def pascal_triangle(n):
    """returns a list of lists of integers representing
    the Pascal's triangle of n
    Args:
        n (int): size of triangle
    """
    superList, current, next = [], [], []

    if n <= 0:
        return []

    current.append(1)
    superList.append(current)
    for i in range(n - 1):
        if len(superList) == 1:
            current = [1, 1]
            superList.append(current)
            continue

        next.append(1)
        for j in range(0, len(current) - 1):
            next.append(current[j] + current[j+1])
        next.append(1)
        superList.append(next)
        current = next
        next = []
    return superList
