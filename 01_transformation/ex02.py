import os.path as osp
import bk7084 as bk
from bk7084.math import *
import numpy as np

window = bk.Window()
window.set_title('BK7084 - Lab 1 - Transformation [ex01]')
window.set_size(1024, 1024)
window.set_resizable(True)

app = bk.App()

camera = app.create_camera(Vec3(-100.0, 50.0, 0.0), Vec3(0, 0, 0), 60.0)

"""
Exercise 2: Hierarchical transformation
-----------------------------------------

For your final assignment, you will apply the transformations you created
and the knowledge about compositions to animate a solar system.

If you're done, your solar system will follow these conditions:
    a. The earth (green planet) rotates around its own axis (y-axis).
    b. The earth also rotates around the sun (yellow 'planet').
    c. The moon (grey 'planet') rotates around its own axis (y-axis).
    d. The moon rotates around the earth.

As you might notice, the order of compositions matters a lot for this exercise.
Another challenge is to rotate the moon around the earth, while the earth rotates around the sun.
For this, you must *re-use* the transformation matrix you use for the earth.

Don't start without a plan, you will end up with a tangle of code that is very hard to understand.
Instead, first design your solar system on paper and write out how to apply the transformations.
If you do it well, you can finish this exercise by only adding about 5 lines of code!

First, copy your finished transformation functions.
If you have copied these, you should see the sun and earth.
You won't see the moon, because it is still at the center of space, covered by the sun.
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

# Set working directory to the folder where this file is located.
cwd = osp.dirname(osp.abspath(__file__))

"""
Here, we load the planets, no need to adjust anything here yet.
"""
earth = app.add_mesh(bk.Mesh.load_from(osp.join(cwd, 'assets/earth.obj')))
earth.set_transform(Mat4.from_scale(Vec3(0.1)))
earth.set_visible(True)

# moon = app.add_mesh(bk.Mesh.load_from(osp.join(cwd, 'assets/moon.obj')))
# moon.set_transform(Mat4.from_scale(Vec3(0.2)))
# moon.set_visible(True)

# sun = app.add_mesh(bk.Mesh.load_from(osp.join(cwd, 'assets/sun.obj')))
# sun.set_transform(Mat4.from_scale(Vec3(0.15)))
# sun.set_visible(True)

"""
This is where you can start building up your transformation matrices.
For example, create a translation matrix for the earth to be placed away from the sun:
"""
earth_translation = translate(40, 0, 0)
moon_to_earth = Mat4.from_translation(Vec3(10, 0, 0))
# TODO: other transformations you might need


"""
You don't need to change the code below to finish the assignment.
"""

earth_transform = earth_translation
moon_transform = moon_to_earth

"""
You will use the time variable `t` to animate the solar system.
It is updated for you in the on_update function.
"""
@app.event
def on_update(input, dt, t):
    """
    This is where you should apply your transformations the the earth and moon.
    Remember that you can apply transformations with apply_transformation() and then().
    Also, you can get the current transformation for an object with
    >>> earth_transformation = earth.transformation
    """

    # TODO: Compute and earth transformation

    # TODO: Compute and moon transformation

    # TODO: Apply transformations to the earth and moon
    pass


app.run(window)
