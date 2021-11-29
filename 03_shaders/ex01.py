import os.path as osp
from bk7084 import Window, app
from bk7084.app.window.input import KeyCode, KeyModifier
from bk7084.geometry import Triangle, Ray, Line, Box
from bk7084.math import Vec3, Mat3, Mat4
from bk7084.misc import PaletteSvg, PaletteDefault
from bk7084.graphics import draw
from bk7084.scene import Mesh


window = Window("BK7084: 03-Shaders [ex01]", width=1024, height=1024)
window.create_camera(Vec3(-100.0, 50.0, 0.0), Vec3(0, 0, 0), Vec3.unit_y(), 60.0)

assignment_directory = osp.dirname(osp.abspath(__file__))
earth = Mesh(osp.join(assignment_directory, 'assets/earth.obj'), color=PaletteDefault.GreenA.as_color())

@window.event
def on_draw(dt):
    draw(earth)

app.init(window)
app.run()