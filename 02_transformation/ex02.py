from bk7084 import Window, app
from bk7084.app.window.input import KeyCode, KeyModifier
from bk7084.geometry import Triangle, Ray, Line, Box
from bk7084.math import Vec3, Mat3, Mat4
from bk7084.misc import PaletteSvg, PaletteDefault
from bk7084.graphics import draw
from bk7084.scene import Mesh


window = Window("BK7084: 02-Transformation [ex02]", width=1024, height=1024)
window.create_camera(Vec3(-200.0, 80.0, 0.0), Vec3(0, 0, 0), Vec3.unit_y(), 60.0,)

"""
Assignment 2: Order of transformations
----------------------------------

Please read the part one of the accompanying PDF file for an explanation of this assignment.

Your tasks:
1. Reuse transformation functions created in the first assignment.
2. Apply any transformation you want to construct the lamp.
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


grid_size = 100
grid_cell_count = 20
grid_cell_size = 2.0 * grid_size / grid_cell_count

# Red cube represents the positive X direction
# Blue cube represents the positive Z direction
cube_x = Mesh('./assets/cube.obj', color=PaletteDefault.RedB.as_color())
cube_x.initial_transformation = Mat4.from_translation(Vec3(100.0, -50, 0.0)) * Mat4.from_scale(Vec3(5.0))
cube_z = Mesh('./assets/cube.obj', color=PaletteDefault.BlueA.as_color())
cube_z.initial_transformation = Mat4.from_translation(Vec3(0.0, -50, 100.0)) * Mat4.from_scale(Vec3(5.0))

"""
They have multiple ways to apply the transformation.
1. apply_transformation: they can pre-compute all transformation together to one matrix

    >>> # some computation 
    >>> mesh.apply_transformation(mat)

2. transformation chaining

    >>> mesh.apply_transformation(mat0).apply_transformation(mat1)
    
    or
    
    >>> mesh.apply_transformation(mat0).then(mat1).then(mat2)
"""

# Different parts of the lamp
lamp = Mesh('./assets/lamp.obj', color=PaletteSvg.DeepSkyBlue.as_color())
# lamp.initial_transformation = Mat4.from_translation(Vec3(50, -52, -50))
lamp.apply_transformation(Mat4.from_translation(Vec3(50, -52, -50)))

# Lamp's base
lamp_base = Mesh('./assets/base.obj', color=PaletteDefault.RedB.as_color())
# lamp_base.initial_transformation = Mat4.from_translation(Vec3(-53, -47, 48))
lamp_base.apply_transformation(Mat4.from_translation(Vec3(-53, -47, 48)))

# Lamp's 1st segment
lamp_seg0 = Mesh('./assets/seg01.obj', color=PaletteDefault.WhiteB.as_color())
# lamp_seg0.initial_transformation = Mat4.from_translation(Vec3(-53, -36, 48))
lamp_seg0.apply_transformation(Mat4.from_translation(Vec3(-53, -36, 48)))

# Lamp's 1st connector
lamp_con0 = Mesh('./assets/con01.obj', color=PaletteDefault.BlackB.as_color())
# lamp_con0.initial_transformation = Mat4.from_translation(Vec3(-55, -23, 48)) * Mat4.from_rotation_y(180, True)
lamp_con0.apply_transformation(Mat4.from_rotation_y(180, True)).then(Mat4.from_translation(Vec3(-55, -23, 48)))

# Lamp's 2nd segment
lamp_seg1 = Mesh('./assets/seg02.obj', color=PaletteDefault.WhiteB.as_color())
# lamp_seg1.initial_transformation = Mat4.from_translation(Vec3(-53, -1, 61)) * Mat4.from_rotation_x(30, True)
lamp_seg1.apply_transformation(Mat4.from_rotation_x(30, True)).then(Mat4.from_translation(Vec3(-53, -1, 61)))

# Lamp's 2nd connector
lamp_con1 = Mesh('./assets/con02.obj', color=PaletteDefault.BlackB.as_color())
# lamp_con1.initial_transformation = Mat4.from_translation(Vec3(-55, 20, 72)) * Mat4.from_rotation_y(180, True)
lamp_con1.apply_transformation(Mat4.from_rotation_y(180, True)).then(Mat4.from_translation(Vec3(-55, 20, 72)))

# Lamp's 3rd segment
lamp_seg2 = Mesh('./assets/seg03.obj', color=PaletteDefault.WhiteB.as_color())
# lamp_seg2.initial_transformation = Mat4.from_translation(Vec3(-53, 40, 58)) * Mat4.from_rotation_x(-39, True)
lamp_seg2.apply_transformation(Mat4.from_rotation_x(-39, True)).then(Mat4.from_translation(Vec3(-53, 40, 58)))

# Lamp's 3rd connector
lamp_con2 = Mesh('./assets/con03.obj', color=PaletteDefault.BlackB.as_color())
# lamp_con2.initial_transformation = Mat4.from_translation(Vec3(-55, 59, 40)) * Mat4.from_rotation_y(180, True)
lamp_con2.apply_transformation(Mat4.from_rotation_y(180, True)).then(Mat4.from_translation(Vec3(-55, 59, 40)))

# Lamp's head
lamp_head = Mesh('./assets/head.obj', color=PaletteDefault.YellowA.as_color())
# lamp_head.initial_transformation = Mat4.from_translation(Vec3(-53, 48, 21)) * Mat4.from_rotation_x(-210, True)
lamp_head.apply_transformation(Mat4.from_rotation_x(-210, True)).then(Mat4.from_translation(Vec3(-53, 48, 21)))

lamp_components = [lamp_base, lamp_seg0, lamp_con0, lamp_seg1, lamp_con1, lamp_seg2, lamp_con2, lamp_head]


@window.event
def on_draw(dt):
    # Draw a grid of lines
    for i in range(grid_cell_count + 1):
        d = i * grid_cell_size
        if i == 10:
            draw(Line([Vec3(-grid_size, -50, -grid_size + d), Vec3(grid_size, -50, -grid_size + d)],
                      (PaletteDefault.RedA.as_color(),)))
            draw(Line([Vec3(-grid_size + d, -50, -grid_size), Vec3(-grid_size + d, -50, grid_size)],
                      (PaletteDefault.BlueA.as_color(),)))
        else:
            draw(Line([Vec3(-grid_size, -50, -grid_size + d), Vec3(grid_size, -50, -grid_size + d)]))
            draw(Line([Vec3(-grid_size + d, -50, -grid_size), Vec3(-grid_size + d, -50, grid_size)]))
    draw(lamp, *lamp_components, cube_x, cube_z)


@window.event
def on_key_press(key, mods):
    if key == KeyCode.Up:
        lamp.apply_transformation(Mat4.from_translation(Vec3(0.5, 0.0, 0.0)))

    if key == KeyCode.Down:
        lamp.apply_transformation(Mat4.from_translation(Vec3(-0.5, 0.0, 0.0)))

    if key == KeyCode.Left:
        lamp.apply_transformation(Mat4.from_translation(Vec3(0.0, 0.0, -0.5)))

    if key == KeyCode.Right:
        lamp.apply_transformation(Mat4.from_translation(Vec3(0.0, 0.0, 0.5)))

    if key == KeyCode.S:
        lamp.apply_transformation(Mat4.from_scale(Vec3(0.9, 0.9, 0.9)))

    if key == KeyCode.R:
        # Ctrl + R to reset transformation
        if KeyModifier.Ctrl in mods:
            lamp.reset_transformation()
        else:
            lamp.apply_transformation(Mat4.from_axis_angle(Vec3.unit_y(), 90.0, True))


app.init(window)
app.run()
