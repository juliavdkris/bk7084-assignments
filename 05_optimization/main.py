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

window = Window("BK7084: Construction", width=1024, height=1024, clear_color=Palette.BlueA.as_color())

"""
Final Assignment Part 2
-----------------------
With your buildings done, you are now ready to build a city and optimize its layout.
For this assignment, you have to complete two files: city.py and optimizer.py.

The first step, as always is to update the framework:
$ conda activate compsim
$ pip install --upgrade bk7084

Once that's done, copy buildings.py and components.py files from the previous assignment into this folder.
With that step complete, you should be able to run this file and see your buildings in the city grid.

Next, you have three main tasks:
1. Complete the '__init__' function in city.py to fill the city.
2. Complete the 'score' function in optimizer.py to compute a score for the city.
3. Complete the 'step' function in optimizer.py to optimize the city and add a stopping criterion in 'optimizer'.

You can test each of these functions by running this file and by using the buttons
'Start', 'Stop', 'One step', 'Optimize offline'

Good luck!
"""
# Construct the city
city = City(name='Grid City', row=8, col=8)
# Set the scene
scene = Scene(window, [city], draw_light=True)
scene.create_camera(Vec3(16, 16, 0), Vec3(0, 0, 0), Vec3.unit_y(), 60, zoom_enabled=True, safe_rotations=True)
# And set up the optimizer
optimizer = Optimizer(city, scene)
run_optimizer = False
plot_row, plot_col = 0, 0
building_row, building_col = 0, 0


@window.event
def on_update(dt):
    global run_optimizer
    if run_optimizer:
        optimizer.step()

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
    global run_optimizer
    if ui.button('Start'):
        run_optimizer = True
    if ui.button('Stop'):
        run_optimizer = False
    if ui.button('One step'):
        optimizer.step(verbose=True)
    if ui.button('Optimize offline'):
        optimizer.optimize()
    if ui.button('Reset'):
        city.reset()

app.init(window)
app.run()
