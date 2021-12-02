import os.path as osp
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
Exercise 3: Hierarchical transformation
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

"""
Here, we load the planets, no need to adjust anything here yet.
"""
assignment_directory = osp.dirname(osp.abspath(__file__))
earth = Mesh(osp.join(assignment_directory, 'assets/earth.obj'), color=PaletteDefault.GreenA.as_color())
earth.initial_transformation = Mat4.from_scale(Vec3(0.1))

moon = Mesh(osp.join(assignment_directory, 'assets/moon.obj'), color=PaletteDefault.WhiteB.as_color())
moon.initial_transformation = Mat4.from_scale(Vec3(0.2))

sun = Mesh(osp.join(assignment_directory, 'assets/sun.obj'), color=PaletteDefault.YellowA.as_color())
sun.initial_transformation = Mat4.from_scale(Vec3(0.15))

"""
This is where you can start building up your transformation matrices.
For example, create a translation matrix for the earth to be placed away from the sun:
"""
earth_translation = translate(30, 0, 0)
# TODO: other transformations you might need

"""
You will use this time variable to animate the solar system.
It is updated for you in the on_update function.
"""
time = 0.0


@window.event
def on_draw(dt):
    draw(sun)

    """
    This is where you should apply your transformations the the earth and moon.
    Remember that you can apply transformations with apply_transformation() and then().
    Also, you can get the current transformation for an object with
    >>> earth_transformation = earth.transformation
    """
    earth.reset_transformation()
    earth.apply_transformation(earth_translation)
    # TODO: Compute and apply transformations
    draw(earth)

    moon.reset_transformation()
    # TODO: Compute and apply transformations
    draw(moon)

"""
You don't need to change the code below to finish the assignment.
"""

@window.event
def on_update(dt):
    global time
    time += dt


app.init(window)
app.run()
