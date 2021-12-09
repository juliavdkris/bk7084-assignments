from bk7084 import Window, app, Camera
from bk7084.app.window.input import KeyCode
from bk7084.math import Vec3, Mat4
from bk7084.misc import PaletteDefault as Palette
from bk7084.graphics import draw, PointLight
from bk7084.scene import Mesh, Building, Component

from buildings import *
from components import *

# Setup window and add camera
window = Window("BK7084: Construction", width=1024, height=1024)
window.create_camera(Vec3(4, 2.0, 4.0), Vec3(0, 0, 0), Vec3.unit_y(), 60.0, zoom_enabled=True)

ground = Ground()

buildings = []
buildings.append(Skyscraper())

@window.event
def on_draw(dt):
    ground.draw()
    for building in buildings:
        building.draw()

@window.event
def on_key_press(key, mods):
    pass


app.init(window)
app.run()
