import os
from bk7084 import Window, app
from bk7084.app.window.input import KeyCode
from bk7084.geometry import Triangle, Ray, Line, Box
from bk7084.math import Vec3, Mat3, Mat4
from bk7084.misc import PaletteSvg, PaletteDefault
from bk7084.graphics import draw, ShaderProgram, VertexShader, PixelShader
from bk7084.scene import Mesh

# Setup window and add camera
window = Window("BK7084: 03-Shaders [ex04]", width=1024, height=1024)
window.create_camera(Vec3(2.0, 1.0, -2.0), Vec3(0, 0, 0), Vec3.unit_y(), 60.0)
assignment_directory = os.path.dirname(os.path.abspath(__file__))

"""
Exercise 4: Advanced fragment shader
------------------------------------

In the previous exercises you got to know the vertex and fragment shader
and found out how to combine the two.
In this exercise, you'll create more advanced looks with the fragment shader.
You have two tasks. Only do the second task if you have the time.
1. Implement a rim light effect (https://www.roxlu.com/2014/037/opengl-rim-shader)
2. Implement a toon color effect (https://www.lighthouse3d.com/tutorials/glsl-12-tutorial/toon-shader-version-ii/)

When you're done with this exercise and still have time left,
you can learn more about shaders by going through the Book of Shaders (https://thebookofshaders.com/00/)
This online book with lots of interactive material can help you grasp shaders even better.

For now, open up `ex04.frag` to continue.
"""

window.default_shader = ShaderProgram(
    VertexShader.from_file(os.path.join(assignment_directory, 'ex04.vert')),
    PixelShader.from_file(os.path.join(assignment_directory, 'ex04.frag'))
)

cow = Mesh(os.path.join(assignment_directory, '../assets/spot.obj'), color=PaletteDefault.RedB.as_color())
cow.shading_enabled = True

animate = True


@window.event
def on_draw(dt):
    draw(cow)


@window.event
def on_key_press(key, mods):
    global animate
    if key == KeyCode.A:
        animate = not animate


@window.event
def on_update(dt):
    if animate:
        cow.apply_transformation(Mat4.from_axis_angle(Vec3.unit_y(), 45.0 * dt, True))


app.init(window)
app.run()
