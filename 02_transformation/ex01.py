from bk7084 import Window, app
from bk7084.app.window.input import KeyCode, KeyModifier
from bk7084.geometry import Triangle, Ray, Line, Box
from bk7084.math import Vec3, Mat3, Mat4
from bk7084.misc import PaletteSvg, PaletteDefault
from bk7084.graphics import draw
from bk7084.scene import Mesh


window = Window("BK7084: 02-Transformation [ex01]", width=1024, height=1024)
window.create_camera(Vec3(-15.0, 8.0, 0.0), Vec3(0, 0, 0), Vec3.unit_y(), 60.0)

'''
Assignment 1: Basic transformation
----------------------------------

Please read the part one of the accompanying PDF file for an explanation of this assignment.

Your tasks:
1. Build transformation matrices (do NOT use built-in functions):
  a. translation matrix 
  b. rotation matrix
  c. scaling matrix
2. Move the car to reach the red cube and blue cube inside
'''


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


cube_x = Mesh('./assets/cube.obj', color=PaletteDefault.RedB.as_color())
cube_x.initial_transformation = Mat4.from_translation(Vec3(8.0, 0.0, 0.0)) * Mat4.from_scale(Vec3(0.2))
cube_z = Mesh('./assets/cube.obj', color=PaletteDefault.BlueA.as_color())
cube_z.initial_transformation = Mat4.from_translation(Vec3(0.0, 0.0, 8.0)) * Mat4.from_scale(Vec3(0.2))
car = Mesh('./assets/car.obj', color=PaletteDefault.RedA.as_color())


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
        car.apply_transformation(Mat4.from_translation(Vec3(0.5, 0.0, 0.0)))

    if key == KeyCode.Down:
        car.apply_transformation(Mat4.from_translation(Vec3(-0.5, 0.0, 0.0)))

    if key == KeyCode.Left:
        car.apply_transformation(Mat4.from_translation(Vec3(0.0, 0.0, -0.5)))

    if key == KeyCode.Right:
        car.apply_transformation(Mat4.from_translation(Vec3(0.0, 0.0, 0.5)))

    if key == KeyCode.S:
        car.apply_transformation(Mat4.from_scale(Vec3(0.9, 0.9, 0.9)))

    if key == KeyCode.R:
        # Ctrl + R to reset transformation
        if KeyModifier.Ctrl in mods:
            car.reset_transformation()
        else:
            car.apply_transformation(Mat4.from_axis_angle(Vec3.unit_y(), 45.0, True))


app.init(window)
app.run()
