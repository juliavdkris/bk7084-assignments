import os
from bk7084 import Window, app
from bk7084.app.window.input import KeyCode
from bk7084.math import Vec3, Mat4
from bk7084.misc import PaletteDefault
from bk7084.graphics import draw, ShaderProgram, VertexShader, PixelShader
from bk7084.scene import Mesh

# Setup window and add camera
window = Window("BK7084: 03-Shaders [ex03]", width=1024, height=1024)
window.create_camera(Vec3(2.0, 1.0, -2.0), Vec3(0, 0, 0), Vec3.unit_y(), 60.0)
assignment_directory = os.path.dirname(os.path.abspath(__file__))

"""
Exercise 3: Vertex to fragment shader
-------------------------------------

Now that you know what you can do in the vertex and fragment shader,
let's see how you can combine the two for some interesting effects.

Remember that you passed variables from the vertex shader to the fragment shader
with the `in` and `out` variables?
In this exercise, you will use these variables and see what happens in-between.
If everything that you output in the vertex shader is defined at the vertices,
how does the fragment shader get information per pixel?

There is a 'hidden' step performed by your GPU, which is interpolation.
Values from the vertices are interpolated to values on the triangles.
In this exercise, we'll experiment with this and use a time variable to animate effects.

Open up `ex03.vert` to continue.
"""

window.default_shader = ShaderProgram(
    VertexShader.from_file(os.path.join(assignment_directory, 'ex03.vert')),
    PixelShader.from_file(os.path.join(assignment_directory, 'ex03.frag'))
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
