import os.path as osp

from bk7084 import Window, app
from bk7084.app.input import KeyCode, KeyModifier
from bk7084.geometry import Triangle, Ray, Line, Box, Grid, AxisAlignment
from bk7084.math import Vec3, Mat3, Mat4
from bk7084.misc import PaletteSvg, PaletteDefault
from bk7084.graphics import draw
from bk7084.scene import Mesh
import numpy as np

window = Window("BK7084: 02-Transformation [ex02]", width=1024, height=1024)
window.create_camera(Vec3(-200.0, 80.0, 0.0), Vec3(0, 0, 0), Vec3.unit_y(), 60.0,)

"""
Exercise 2: Composing transformations
-------------------------------------

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
lamp = Mesh('lamp', osp.join('assets/lamp.obj'), colors=(PaletteSvg.DeepSkyBlue.as_color(),))
lamp.apply_transform(translate(50, -52, -50))

# Lamp's base
lamp_base = Mesh('lamp-base', osp.join('assets/base.obj'), colors=(PaletteDefault.RedB.as_color(),))
lamp_base.apply_transform(translate(-53, -47, 48))

# Lamp's 1st segment
lamp_seg0 = Mesh('lamp-seg0', osp.join('assets/seg01.obj'), colors=(PaletteDefault.WhiteB.as_color(),))
lamp_seg0.apply_transform(translate(-53, -36, 48))

# Lamp's 1st connector
lamp_con0 = Mesh('lamp-con0', osp.join('assets/con01.obj'), colors=(PaletteDefault.BlackB.as_color(),))
# TODO: Place in the right configuration

# Lamp's 2nd segment
lamp_seg1 = Mesh('lamp-seg1', osp.join('assets/seg02.obj'), colors=(PaletteDefault.WhiteB.as_color(),))
# TODO: Place in the right configuration

# Lamp's 2nd connector
lamp_con1 = Mesh('lamp-con1', osp.join('assets/con02.obj'), colors=(PaletteDefault.BlackB.as_color(),))
# TODO: Place in the right configuration

# Lamp's 3rd segment
lamp_seg2 = Mesh('lamp-seg2', osp.join('assets/seg03.obj'), colors=(PaletteDefault.WhiteB.as_color(),))
# TODO: Place in the right configuration

# Lamp's 3rd connector
lamp_con2 = Mesh('lamp-con2', osp.join('assets/con03.obj'), colors=(PaletteDefault.BlackB.as_color(),))
# TODO: Place in the right configuration

# Lamp's head
lamp_head = Mesh('lamp-head', osp.join('assets/head.obj'), colors=(PaletteDefault.YellowA.as_color(),))
# TODO: Place in the right configuration

"""
You don't need to change the code below to finish the assignment.
"""

lamp_components = [lamp_base, lamp_seg0, lamp_con0, lamp_seg1, lamp_con1, lamp_seg2, lamp_con2, lamp_head]

# Disable materials to show colors
lamp.material_enabled = False
for c in lamp_components:
    c.material_enabled = True

grid = Grid(width=200.0, height=200.0, spacing_width=5.0, spacing_height=5.0,
            origin=Vec3(0.0, -50, 0.0), axis_alignment=AxisAlignment.XZ, axis_marker=True)

@window.event
def on_draw(dt):
    draw(lamp, *lamp_components, grid)


@window.event
def on_key_press(key, mods):
    if key == KeyCode.Up:
        lamp.apply_transform(translate(0.5, 0.0, 0.0))

    if key == KeyCode.Down:
        lamp.apply_transform(translate(-0.5, 0.0, 0.0))

    if key == KeyCode.Left:
        lamp.apply_transform(translate(0.0, 0.0, -0.5))

    if key == KeyCode.Right:
        lamp.apply_transform(translate(0.0, 0.0, 0.5))

    if key == KeyCode.X:
        lamp.apply_transform(rotate_x(90.0))

    if key == KeyCode.Y:
        lamp.apply_transform(rotate_y(90.0))

    if key == KeyCode.Z:
        lamp.apply_transform(rotate_z(90.0))

    if key == KeyCode.S:
        lamp.apply_transform(scale(0.9, 0.9, 0.9))

    if key == KeyCode.R:
        lamp.reset_transform()


app.init(window)
app.run()
