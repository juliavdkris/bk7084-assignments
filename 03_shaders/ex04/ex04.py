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
