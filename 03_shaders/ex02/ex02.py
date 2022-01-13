import os
from bk7084 import Window, app
from bk7084.app.input import KeyCode
from bk7084.math import Vec3, Mat4
from bk7084.misc import PaletteDefault
from bk7084.graphics import draw, ShaderProgram, VertexShader, PixelShader
from bk7084.scene import Mesh

# Setup window and add camera
window = Window("BK7084: 03-Shaders [ex02]", width=1024, height=1024)
window.create_camera(Vec3(2.0, 1.0, -2.0), Vec3(0, 0, 0), Vec3.unit_y(), 60.0)

"""
Exercise 2: Fragment shader
---------------------------

In the previous exercise, you used shaders to modify vertex positions.
After the vertex shader is done, your GPU runs a couple of fixed operations that you cannot program.
For example, the GPU interpolates values on the vertices to values on the triangles.
Next, the fragment shader is run. In this exercise you will experiment with the fragment shader
and try a couple of simple operations to become acquainted.

Try running this file first. Different from the last exercise, the cow now has different colours.
This is achieved using a *texture*. A texture is an image that is wrapped around a 3D object.
The way this is done is by matching each vertex with a coordinate in the texture, a texture coordinate.

In the exercise, you will try a couple of operations to change the colour of the texture.
One example is thresholding the texture based on the intensity of the colour.

Open up `ex02.frag` to continue.
"""

window.default_shader = ShaderProgram(
    VertexShader.from_file(os.path.join('ex02.vert')),
    PixelShader.from_file(os.path.join('ex02.frag'))
)

cow = Mesh(os.path.join('../assets/spot.obj'), color=PaletteDefault.RedB.as_color())

# Disable/enable shading
cow.shading_enabled = True

animate = False

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
