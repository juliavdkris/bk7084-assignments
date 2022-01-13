from bk7084 import Window, app
from bk7084.math import Vec3, Mat4
from bk7084.misc import PaletteDefault as Palette
from bk7084.scene import Mesh, Scene
from bk7084.app.input import KeyCode
from bk7084.app import ui

from city import City
from optimizer import Optimizer
try:
    from buildings import *
    from components import *
except ModuleNotFoundError as e:
    raise ModuleNotFoundError('Buildings or components not found, please copy-paste buildings.py and components.py from 04_buildinggeneration into this folder.') from e

# Setup window and add camera
window = Window("BK7084: Construction", width=1024, height=1024, clear_color=Palette.BlueA.as_color())

city = City()

scene = Scene(window, [city], draw_light=True)
scene.create_camera(Vec3(16, 16, 0), Vec3(0, 0, 0), Vec3.unit_y(), 60, zoom_enabled=True, safe_rotations=True)

optimizer = Optimizer(scene, city)

comp = 0
building = 0

@window.event
def on_draw(dt):
    scene.draw_v2(auto_shadow=True)
    city.grid.draw_grid_line()

@window.event
def on_gui():
    if ui.button('Optimize'):
        optimizer.optimize()


@window.event
def on_key_press(key, mods):
    # if key == KeyCode.C:
    #     scene.energy_of_building_component(buildings[building], buildings[building].components[comp], save_energy_map=True)

    # if key == KeyCode.B:
    #     scene.energy_of_building(buildings[building], save_energy_map=True)
    return

app.init(window)
app.run()
