from bk7084 import Window, app
from bk7084.app.window.input import KeyCode, KeyModifier
from bk7084.geometry import Triangle, Ray, Line, Box
from bk7084.math import Vec3, Mat3, Mat4
from bk7084.misc import PaletteSvg, PaletteDefault
from bk7084.graphics import draw
from bk7084.scene import Mesh
import numpy as np


window = Window("BK7084: 02-Transformation [ex02]", width=1024, height=1024)
window.create_camera(Vec3(-200.0, 80.0, 0.0), Vec3(0, 0, 0), Vec3.unit_y(), 60.0,)

"""
Exercise 2: Composing transformations
---------------------------------------

You are going to construct a virtual lamp by composing transformation matrices.
When you first run this program, you will see a blue lamp in the far-left corner.
There's also a lamp base at the opposite corner in red and components of the lamp at the center.
It's up to you to place the components of the red lamp in the right position on the base of the lamp.

Be sure to read section 4 in the accompanying PDF before you start this exercise.

First, copy the transformation matrix construction functions from ex01 here:
"""
# TODO copy the completed functions from ex01

def translate(x: float, y: float, z: float) -> Mat4:
    return Mat4.identity()

def rotate_x(angle: float) -> Mat4:
    return Mat4.identity()

def rotate_y(angle: float) -> Mat4:
    return Mat4.identity()

def rotate_z(angle: float) -> Mat4:
    return Mat4.identity()

def scale(x: float, y: float, z: float) -> Mat4:
    return Mat4.identity()

"""
Next, transform the lamp components to put them in the right position.
If you're unsure if you've positioned components correctly,
you can rotate the blue lamp to the close corner with [Y] (rotate around y-axis).

You have two ways to apply a transformation.
1. apply_transformation: compose transformation together to one matrix and apply to the mesh:
    >>> mat = rotate_y(45) * rotate_x(45) * translate(10, 0, 0)
    >>> mesh.apply_transformation(mat)

2. chaining transformations
    >>> mesh.apply_transformation(mat0).apply_transformation(mat1)
    or  
    >>> mesh.apply_transformation(mat0).then(mat1).then(mat2)

Note that the order you multiply transformation matrices is the reverse of chaining transformations.
"""

# Different parts of the lamp
# Lamp model by https://sketchfab.com/Bharad CC BY 4.0
lamp = Mesh('./assets/lamp.obj', color=PaletteSvg.DeepSkyBlue.as_color())
lamp.apply_transformation(translate(50, -52, -50))

# Lamp's base
lamp_base = Mesh('./assets/base.obj', color=PaletteDefault.RedB.as_color())
lamp_base.apply_transformation(translate(-53, -47, 48))

# Lamp's 1st segment
lamp_seg0 = Mesh('./assets/seg01.obj', color=PaletteDefault.WhiteB.as_color())
lamp_seg0.apply_transformation(translate(-53, -36, 48))

# Lamp's 1st connector
lamp_con0 = Mesh('./assets/con01.obj', color=PaletteDefault.BlackB.as_color())
# TODO: Place in the right configuration

# Lamp's 2nd segment
lamp_seg1 = Mesh('./assets/seg02.obj', color=PaletteDefault.WhiteB.as_color())
# TODO: Place in the right configuration

# Lamp's 2nd connector
lamp_con1 = Mesh('./assets/con02.obj', color=PaletteDefault.BlackB.as_color())
# TODO: Place in the right configuration

# Lamp's 3rd segment
lamp_seg2 = Mesh('./assets/seg03.obj', color=PaletteDefault.WhiteB.as_color())
# TODO: Place in the right configuration

# Lamp's 3rd connector
lamp_con2 = Mesh('./assets/con03.obj', color=PaletteDefault.BlackB.as_color())
# TODO: Place in the right configuration

# Lamp's head
lamp_head = Mesh('./assets/head.obj', color=PaletteDefault.YellowA.as_color())
# TODO: Place in the right configuration

"""
You don't need to change the code below to finish the assignment.
"""

lamp_components = [lamp_base, lamp_seg0, lamp_con0, lamp_seg1, lamp_con1, lamp_seg2, lamp_con2, lamp_head]

grid_size = 100
grid_cell_count = 20
grid_cell_size = 2.0 * grid_size / grid_cell_count

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
    draw(lamp, *lamp_components)


@window.event
def on_key_press(key, mods):
    if key == KeyCode.Up:
        lamp.apply_transformation(translate(0.5, 0.0, 0.0))

    if key == KeyCode.Down:
        lamp.apply_transformation(translate(-0.5, 0.0, 0.0))

    if key == KeyCode.Left:
        lamp.apply_transformation(translate(0.0, 0.0, -0.5))

    if key == KeyCode.Right:
        lamp.apply_transformation(translate(0.0, 0.0, 0.5))

    if key == KeyCode.X:
        lamp.apply_transformation(rotate_x(90.0))

    if key == KeyCode.Y:
        lamp.apply_transformation(rotate_y(90.0))   

    if key == KeyCode.Z:
        lamp.apply_transformation(rotate_z(90.0))   

    if key == KeyCode.S:
        lamp.apply_transformation(scale(0.9, 0.9, 0.9))

    if key == KeyCode.R:
        lamp.reset_transformation()


app.init(window)
app.run()
