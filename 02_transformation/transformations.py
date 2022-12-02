import numpy as np
from bk7084.math import Mat4

"""
TODO: Implement the transformation matrices for ex01 in the functions below.
"""

def translate(x: float, y: float, z: float) -> Mat4:
    """
    Creates a translation matrix.

    Args:
        x (float): Translation along the x-axis.
        y (float): Translation along the y-axis
        z (float): Translation along the z-axis

    Returns:
        Mat4
    """
    # TODO: complete this matrix
    mat = Mat4(
        [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ]
    )
    return mat


def rotate_x(angle: float) -> Mat4:
    """
    Creates a rotation matrix around the x-axis.

    Args:
        angle (float): Rotation angle in degrees.

    Returns:
        Mat4
    """
    # TODO: complete this matrix
    # hint: you can compute cos and sin with np.cos(angle) and np.sin(angle)
    mat = Mat4(
        [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ]
    )
    return mat


def rotate_y(angle: float) -> Mat4:
    """
    Creates a rotation matrix around the y-axis.

    Args:
        angle (float): Rotation angle in degrees.

    Returns:
        Mat4
    """
    # TODO: complete this matrix
    # hint: you can compute cos and sin with np.cos(angle) and np.sin(angle)
    mat = Mat4(
        [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ]
    )
    return mat


def rotate_z(angle: float) -> Mat4:
    """
    Creates a rotation matrix around the z-axis.

    Args:
        angle (float): Rotation angle in degrees.

    Returns:
        Mat4
    """
    # TODO: complete this matrix
    # hint: you can compute cos and sin with np.cos(angle) and np.sin(angle)
    mat = Mat4(
        [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ]
    )
    return mat


def scale(x: float, y: float, z: float) -> Mat4:
    """
    Creates a scaling matrix.

    Args:
        x (float): Scaling factor along x-axis.
        y (float): Scaling factor along y-axis.
        z (float): Scaling factor along z-axis.

    Returns:
        Mat4
    """
    # TODO: complete this matrix
    mat = Mat4(
        [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ]
    )
    return mat