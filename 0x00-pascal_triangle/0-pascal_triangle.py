#!/usr/bin/python3

"""A file that constructs a list of lists of integers
representing Pascal's Triangle
"""


def pascal_triangle(n):
    """This function constructs Pascal's Triangle"""
    if n <= 0:
        return []
    pascals_triangle = [[1]]
    for i in range(1, n):
        prev_row = pascals_triangle[i - 1]
        current_row = [1]

        for j in range(1, i):
            current_row.append(prev_row[j - 1] + prev_row[j])
        current_row.append(1)
        pascals_triangle.append(current_row)
    return pascals_triangle
