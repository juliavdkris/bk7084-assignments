import bk7084 as bk
from buildings import *


win = bk.Window()
win.set_title("BK7084 - Lab 4 - Building Generation [ex03]")
win.set_size(800, 800)
win.set_resizable(True)

app = bk.App()
camera = app.create_camera(
    pos=Vec3(16, 18, 26), look_at=Vec3(0, 0, 0), fov_v=60.0, background=bk.Color.ICE_BLUE
)
camera.set_as_main_camera()

app.add_directional_light(Vec3(0, 0, -1), bk.Color(0.8, 0.8, 0.8))

skyscraper = Skyscraper(app, 5, 3)
skyscraper.building.set_transform(Mat4.identity())

highrise = Skyscraper(app, 3, 3)
highrise.building.set_transform(Mat4.from_translation(Vec3(5, 0, 0)))

office = Skyscraper(app, 2, 3)
office.building.set_transform(Mat4.from_translation(Vec3(-5, 0, 0)))

# Variables to avoid key spamming
is_key_1_pressed = False
is_key_2_pressed = False

enable_backface_culling = True
enable_wireframe = False

app.enable_backface_culling(enable_backface_culling)
app.enable_wireframe(enable_wireframe)


@app.event
def on_update(input, dt, t):
    global enable_backface_culling
    global enable_wireframe
    global is_key_1_pressed
    global is_key_2_pressed

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


app.run(win)
