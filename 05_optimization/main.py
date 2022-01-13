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
plot_row, plot_col = 0, 0
building_row, building_col = 0, 0

@window.event
def on_draw(dt):
    scene.draw_v2(auto_shadow=True)
    city.grid.draw_grid_line()

@window.event
def on_gui():
    global plot_row, plot_col, building_col, building_row
    if ui.tree_node('Optimization'):
        if ui.tree_node('Plot info'):
            _, (plot_row, plot_col) = ui.drag_int2('Location', plot_row, plot_col)
            plot_row %= 8
            plot_col %= 8
            if ui.button('Compute Energy'):
                e = optimizer.compute_light_of_plot(plot_row, plot_col, scene.current_light)
                print(f'energy of plot [{plot_row},{plot_col}] = {e}')
            ui.tree_pop()
        if ui.tree_node('Building info'):
            _, (building_row, building_col) = ui.drag_int2('Location', building_row, building_col)
            building_row %= 8
            building_col %= 8
            if ui.button('Compute Energy'):
                e = optimizer.compute_light_of_building(building_row, building_col, scene.current_light)
                print(f'energy of building [{building_row},{building_col}] = {e}')
            ui.tree_pop()
        if ui.button('Optimize'):
            optimizer.optimize()
        ui.tree_pop()

@window.event
def on_key_press(key, mods):
    # if key == KeyCode.C:
    #     scene.energy_of_building_component(buildings[building], buildings[building].components[comp], save_energy_map=True)

    # if key == KeyCode.B:
    #     scene.energy_of_building(buildings[building], save_energy_map=True)
    return

app.init(window)
app.run()
