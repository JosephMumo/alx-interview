#!/usr/bin/python3
'''A 2D matrix rotation operation'''


def rotate_2d_matrix(matrix):
    '''rotates the 2d matrix 90° clockwise
    Returns: Nothing to return here'''
    left, right = 0, len(matrix) - 1

    while left < right:
        for i in range(right - left):
            top, bottom = left, right
            topLeft = matrix[top][left + i]
            matrix[top][left + i] = matrix[bottom - i][left]
            matrix[bottom - i][left] = matrix[bottom][right - i]
            matrix[bottom][right - i] = matrix[top + i][right]
            matrix[top + i][right] = topLeft
        right -= 1
        left += 1
