import os.path as osp
from bk7084 import Window, app
from bk7084.app.window.input import KeyCode, KeyModifier
from bk7084.geometry import Triangle, Ray, Line, Box
from bk7084.math import Vec3, Mat3, Mat4
from bk7084.misc import PaletteSvg, PaletteDefault
from bk7084.graphics import draw
from bk7084.scene import Mesh
import numpy as np


window = Window("BK7084: 02-Transformation [ex01]", width=1024, height=1024)
window.create_camera(Vec3(-15.0, 8.0, 0.0), Vec3(0, 0, 0), Vec3.unit_y(), 60.0)

"""
Exercise 1: Basic transformation
----------------------------------

First update your bk7084 package with pip:
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

assignment_directory = osp.dirname(osp.abspath(__file__))
cube_x = Mesh(osp.join(assignment_directory, 'assets/cube.obj'), color=PaletteDefault.RedB.as_color())
cube_x.initial_transformation = Mat4.from_translation(Vec3(8.0, 0.0, 0.0)) * Mat4.from_scale(Vec3(0.2))
cube_z = Mesh(osp.join(assignment_directory, 'assets/cube.obj'), color=PaletteDefault.BlueA.as_color())
cube_z.initial_transformation = Mat4.from_translation(Vec3(0.0, 0.0, 8.0)) * Mat4.from_scale(Vec3(0.2))
car = Mesh(osp.join(assignment_directory, 'assets/car.obj'), color=PaletteDefault.RedA.as_color())


@window.event
def on_draw(dt):
    # Draw a grid of lines
    for i in range(21):
        if i == 10:
            draw(Line([Vec3(-10, -1.1, -10 + i), Vec3(10, -1.1, -10 + i)], (PaletteDefault.RedA.as_color(),)))
            draw(Line([Vec3(-10 + i, -1.1, -10), Vec3(-10 + i, -1.1, 10)], (PaletteDefault.BlueA.as_color(),)))
        else:
            draw(Line([Vec3(-10, -1.1, -10 + i), Vec3(10, -1.1, -10 + i)]))
            draw(Line([Vec3(-10 + i, -1.1, -10), Vec3(-10 + i, -1.1, 10)]))
    draw(car, cube_x, cube_z)


@window.event
def on_key_press(key, mods):
    if key == KeyCode.Up:
        car.apply_transformation(translate(0.5, 0.0, 0.0))

    if key == KeyCode.Down:
        car.apply_transformation(translate(-0.5, 0.0, 0.0))

    if key == KeyCode.Left:
        car.apply_transformation(translate(0.0, 0.0, -0.5))

    if key == KeyCode.Right:
        car.apply_transformation(translate(0.0, 0.0, 0.5))

    if key == KeyCode.X:
        car.apply_transformation(rotate_x(45))

    if key == KeyCode.Y:
        car.apply_transformation(rotate_y(45))   

    if key == KeyCode.Z:
        car.apply_transformation(rotate_z(45))   

    if key == KeyCode.S:
        car.apply_transformation(scale(0.9, 0.9, 0.9))

    if key == KeyCode.R:
        car.reset_transformation()


app.init(window)
app.run()
