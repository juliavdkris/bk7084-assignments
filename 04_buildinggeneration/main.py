from bk7084 import Window, app
from bk7084.graphics import draw
from bk7084.geometry import Line
from bk7084.math import Vec3, Mat4
from bk7084.misc import PaletteDefault as Palette

from buildings import *
from components import *

# Setup window and add camera
window = Window("BK7084: Construction", width=1024, height=1024, clear_color=Palette.BlueA.as_color())
window.create_camera(Vec3(8, 6, 8), Vec3(0, 0, 0), Vec3.unit_y(), 60, zoom_enabled=True, safe_rotations=True)

ground = Ground(w=40)

buildings = []
buildings.append(Skyscraper(1, 1))

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
