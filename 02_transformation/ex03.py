from bk7084 import Window, app
from bk7084.app.window.input import KeyCode, KeyModifier
from bk7084.geometry import Triangle, Ray, Line, Box
from bk7084.math import Vec3, Mat3, Mat4
from bk7084.misc import PaletteSvg, PaletteDefault
from bk7084.graphics import draw
from bk7084.scene import Mesh


window = Window("BK7084: 02-Transformation [ex03]", width=1024, height=1024)
window.create_camera(Vec3(-100.0, 50.0, 0.0), Vec3(0, 0, 0), Vec3.unit_y(), 60.0)

"""
Assignment 3: Hierarchical transformation
=======

Please read the part one of the accompanying PDF file for an explanation of this assignment.

Your tasks:
1. Build the simplified solar system.
    a. Rotation of the earth (rotate around Y axis)
    b. Revolution of the earth (around the sun)
    c. Rotation of the moon (rotate around Y axis)
    d. Revolution of the moon (around the the earth)
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
    # mat = Mat4(
    #     [
    #         [0, 0, 0, 0],
    #         [0, 0, 0, 0],
    #         [0, 0, 0, 0],
    #         [0, 0, 0, 0]
    #     ]
    # )
    return Mat4.identity()


def rotate_x(angle: float, degrees=False) -> Mat4:
    """
    Creates a rotation matrix around the x-axis.

    Args:
        angle (float): Rotation angle, in radians by default.
        degrees (bool): Specifies how we treat the angle.

    Returns:
        Mat4
    """
    return Mat4.identity()


def rotate_y(angle: float, degrees=False) -> Mat4:
    """
    Creates a rotation matrix around the y-axis.

    Args:
        angle (float): Rotation angle, in radians by default.
        degrees (bool): Specifies how we treat the angle.

    Returns:
        Mat4
    """
    return Mat4.identity()


def rotate_z(angle: float, degrees=False) -> Mat4:
    """
    Creates a rotation matrix around the z-axis.

    Args:
        angle (float): Rotation angle, in radians by default.
        degrees (bool): Specifies how we treat the angle.

    Returns:
        Mat4
    """
    return Mat4.identity()


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
    return Mat4.identity()


earth = Mesh('./assets/earth.obj', color=PaletteDefault.GreenA.as_color())
earth.initial_transformation = Mat4.from_scale(Vec3(0.1))

moon = Mesh('./assets/moon.obj', color=PaletteDefault.WhiteB.as_color())
moon.initial_transformation = Mat4.from_scale(Vec3(0.2))

sun = Mesh('./assets/sun.obj', color=PaletteDefault.YellowA.as_color())
sun.initial_transformation = Mat4.from_scale(Vec3(0.15))

earth_to_sun = Mat4.from_translation(Vec3(30, 0, 0))

moon_to_earth = Mat4.from_translation(Vec3(10, 0, 0))


time = 0.0


@window.event
def on_draw(dt):
    draw(sun)

    earth.reset_transformation()
    earth.transformation = Mat4.from_rotation_y(time * 0.9) * earth_to_sun * Mat4.from_rotation_y(time * 1.2)
    draw(earth)

    moon.reset_transformation()
    moon.apply_transformation(Mat4.from_rotation_y(time)).then(moon_to_earth).then(Mat4.from_rotation_y(time)).then(earth.transformation)
    draw(moon)


@window.event
def on_update(dt):
    global time
    time += dt


app.init(window)
app.run()
