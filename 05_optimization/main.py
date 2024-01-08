import bk7084 as bk
from buildings import *
from city import City
from optimizer import Optimizer

"""
Exercise 04: Building Generation
--------------------------------
"""

win = bk.Window()
win.set_title("BK7084 - Lab 5 - City Optimization")
win.set_size(800, 800)
win.set_resizable(True)

app = bk.App()
camera = app.create_camera(
    pos=Vec3(18, 18, 26),
    look_at=Vec3(0, 0, 0),
    fov_v=60.0,
    near=0.1,
    far=360.0,
    background=bk.Color.ICE_BLUE,
)
camera.set_as_main_camera()

inclination = np.pi / 8
center_pos = Vec3(0, np.cos(inclination), np.sin(inclination))
starting_pos = Mat3.from_rotation_z(-np.pi * 0.5) * center_pos
light = app.add_directional_light(Vec3(0.0) - starting_pos, bk.Color(0.8, 0.8, 0.8))

city = City(app, 32, 32, 3)
optimizer = Optimizer(city)
run_optimizer = False

# Variables to avoid key spamming
is_key_1_pressed = False
is_key_2_pressed = False
is_key_j_pressed = False
is_key_k_pressed = False
is_key_l_pressed = False
is_key_o_pressed = False

enable_backface_culling = True
enable_wireframe = False
app.enable_backface_culling(enable_backface_culling)
app.enable_wireframe(enable_wireframe)
app.enable_shadows(True)
light_rotation = Mat3.identity()
dynamic_light = False
ground_visibility = True


@app.event
def on_update(input, dt, t):
    global enable_backface_culling
    global enable_wireframe
    global is_key_1_pressed
    global is_key_2_pressed
    global is_key_j_pressed
    global is_key_k_pressed
    global is_key_l_pressed
    global is_key_o_pressed
    global light_rotation
    global dynamic_light
    global ground_visibility
    global run_optimizer

    if input.is_key_pressed(bk.KeyCode.Key1):
        if not is_key_1_pressed:
            is_key_1_pressed = True
            enable_backface_culling = not enable_backface_culling
            app.enable_backface_culling(enable_backface_culling)
    if input.is_key_released(bk.KeyCode.Key1):
        is_key_1_pressed = False

    if input.is_key_pressed(bk.KeyCode.Key2):
        if not is_key_2_pressed:
            is_key_2_pressed = True
            enable_wireframe = not enable_wireframe
            app.enable_wireframe(enable_wireframe)
    if input.is_key_released(bk.KeyCode.Key2):
        is_key_2_pressed = False

    if input.is_key_pressed(bk.KeyCode.J):
        if not is_key_j_pressed:
            is_key_j_pressed = True
            dynamic_light = not dynamic_light
    if input.is_key_released(bk.KeyCode.J):
        is_key_j_pressed = False

    if input.is_key_pressed(bk.KeyCode.K):
        if not is_key_k_pressed:
            is_key_k_pressed = True
            ground_visibility = not ground_visibility
            city.set_ground_visibility(ground_visibility)
    if input.is_key_released(bk.KeyCode.K):
        is_key_k_pressed = False

    if input.is_key_pressed(bk.KeyCode.L):
        if not is_key_l_pressed:
            is_key_l_pressed = True
            optimizer.step(True)
    if input.is_key_released(bk.KeyCode.L):
        is_key_l_pressed = False

    if input.is_key_pressed(bk.KeyCode.O):
        if not is_key_o_pressed:
            is_key_o_pressed = True
            run_optimizer = not run_optimizer
    if input.is_key_released(bk.KeyCode.O):
        is_key_o_pressed = False

    city.update(dt, t)

    if dynamic_light:
        light_rotation = Mat3.from_rotation_z(dt * 0.2) * light_rotation
        pos = light_rotation * starting_pos
        if pos.y >= 0.0:
            light.set_directional_light(Vec3(0.0) - pos)
            app.enable_lighting(True)
        else:
            light_rotation = Mat3.from_rotation_z(dt * 0.4) * light_rotation
            app.enable_lighting(False)
    else:
        pos = light_rotation * starting_pos
        light.set_directional_light(Vec3(0.0) - pos)

    if run_optimizer:
        optimizer.step()


app.run(win)
