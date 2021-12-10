from bk7084 import Window, app
from bk7084.math import Vec3, Mat4
from bk7084.misc import PaletteDefault as Palette

from buildings import *
from components import *

# Setup window and add camera
window = Window("BK7084: Construction", width=1024, height=1024, clear_color=Palette.BlueA.as_color())
window.create_camera(Vec3(8, 6, 8), Vec3(0, 0, 0), Vec3.unit_y(), 60, zoom_enabled=True, safe_rotations=True)

"""
Before you start, make sure that you have activated the conda environment
and upgraded the bk7084 package to support buildings and components.

$ conda activate compsim
$ pip install --upgrade bk7084
"""

ground = Ground(w=10)

skyscraper = Skyscraper(num_floors=5, max_width=1)
skyscraper.transform = Mat4.identity()

# Remove Skyscraper and uncomment Highrise to draw your Highrise building
highrise = Skyscraper(num_floors=2, max_width=0.8) # Highrise(num_floors=3, max_width=1)
highrise.transform = Mat4.from_translation(Vec3(-2, 0, 0))

# Remove Skyscraper and uncomment Office to draw your Office building
office = Skyscraper(num_floors=1, max_width=1.2) # Office(num_floors=3, max_width=1)
office.transform = Mat4.from_translation(Vec3(2, 0, 0))

buildings = [skyscraper, highrise, office]


@window.event
def on_draw(dt):
    ground.draw()
    for building in buildings:
        building.draw()


app.init(window)
app.run()
