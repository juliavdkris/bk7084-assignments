import os.path as osp
from bk7084 import Window, app
from bk7084.app.input import KeyCode, KeyModifier
from bk7084.geometry import Triangle, Ray, Line, Box, Grid
from bk7084.geometry.grid import AxisAlignment
from bk7084.math import Vec3, Mat3, Mat4
from bk7084.misc import PaletteSvg, PaletteDefault
from bk7084.graphics import draw
from bk7084.scene import Mesh
import numpy as np


window = Window("BK7084: 02-Transformation [ex01]", width=1024, height=1024)
window.create_camera(Vec3(-15.0, 8.0, 0.0), Vec3(0, 0, 0), Vec3.unit_y(), 60.0)

"""
Exercise 1: Basic transformation
--------------------------------

First update your bk7084 package with pip. Type this in the terminal window:
$ conda activate compsim
$ pip install --upgrade bk7084

Make sure that you have also activated the compsim environment in Visual Studio Code (bottom left, Python 3...)

In this first exercise, you will create transformation matrices from scratch.
If you succeed, you can control a virtual car with your keyboard when you run this file:
[up, down, left, right] translate the car forward, backward, left, or right;
[X] rotate the car 45 degrees around the x-axis;
[Y] rotate the car 45 degrees around the y-axis;
[Z] rotate the car 45 degrees around the z-axis;
[S] scale the car to 90%;
[R] reset the car to its original position;
[esc] close the window (faster than clicking the close button).

Please read the accompanying PDF for an introduction and reference to complete this assignment.

Your tasks:
1. Build transformation matrices (do NOT use built-in functions):
  a. translation matrix,
  b. rotation matrices,
  c. scaling matrix.
2. Move the car to reach the red cube and blue cube.
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


"""
You don't need to change the code below to finish the assignment.
"""
car = Mesh('car', './assets/car.obj')
grid = Grid(origin=Vec3(0.0, -1.17, 0.0), axis_alignment=AxisAlignment.XZ, axis_marker=True)
arrows = [
    Mesh('x-axis', './models/arrow.obj', colors=(PaletteDefault.RedB.as_color()), material_enabled=False),
    Mesh('y-axis', './models/arrow.obj', colors=(PaletteDefault.GreenB.as_color()), material_enabled=False),
    Mesh('z-axis', './models/arrow.obj', colors=(PaletteDefault.BlueB.as_color()), material_enabled=False),
]
arrows[0].init_transform = Mat4.from_translation(Vec3(7.0, 0.0, 0.0)) * Mat4.from_scale(Vec3(0.2)) * Mat4.from_rotation_z(-90.0, degrees=True)
arrows[1].init_transform = Mat4.from_translation(Vec3(0.0, 7.0, 0.0)) * Mat4.from_scale(Vec3(0.2))
arrows[2].init_transform = Mat4.from_translation(Vec3(0.0, 0.0, 7.0)) * Mat4.from_scale(Vec3(0.2)) * Mat4.from_rotation_x(90.0, degrees=True)


@window.event
def on_draw(dt):
    draw(grid, car, *arrows)


@window.event
def on_key_press(key, mods):
    if key == KeyCode.Up:
        car.apply_transform(translate(0.5, 0.0, 0.0))

    if key == KeyCode.Down:
        car.apply_transform(translate(-0.5, 0.0, 0.0))

    if key == KeyCode.N:
        car.apply_transform(translate(0.0, 0.5, 0.0))

    if key == KeyCode.M:
        car.apply_transform(translate(0.0, -0.5, 0.0))

    if key == KeyCode.Left:
        car.apply_transform(translate(0.0, 0.0, -0.5))

    if key == KeyCode.Right:
        car.apply_transform(translate(0.0, 0.0, 0.5))

    if key == KeyCode.X:
        car.apply_transform(rotate_x(45))

    if key == KeyCode.Y:
        car.apply_transform(rotate_y(45))

    if key == KeyCode.Z:
        car.apply_transform(rotate_z(45))

    if key == KeyCode.S:
        car.apply_transform(scale(0.9, 0.9, 0.9))

    if key == KeyCode.R:
        car.reset_transform()


app.init(window)
app.run()
