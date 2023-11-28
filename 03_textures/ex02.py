import bk7084 as bk
from bk7084.math import *

win = bk.Window()
win.set_title('BK7084 - Lab 3 - Textures & Shading [ex02]')
win.set_size(1024, 1024)
win.set_resizable(True)

app = bk.App()

camera = app.create_camera(pos=Vec3(2, 0, 8), look_at=Vec3(0, 0, 0), fov_v=60.0, background=bk.Color.ICE_BLUE)
camera.set_as_main_camera()

pl = app.add_point_light(Vec3(0, 0, 5.2), bk.Color(0.8, 0.8, 0.8), show_light=True)

mat = bk.Material()
mat.diffuse = bk.Color(0.9, 0.8, 0.8)
mat.shininess = 32.0
mat.specular = bk.Color(0.0, 0.9, 0.0)
mat.ambient = bk.Color(0.1, 0.1, 0.1)
mat.textures = {
    "diffuse_texture": bk.res_path("./assets/stone_bricks_col.jpg"),
    # "normal_texture": bk.res_path("./assets/stone_bricks_nrm.png"),
    # "normal_texture": bk.res_path("./assets/mosaic_tiles_nrm.png"),
    "normal_texture": bk.res_path("./assets/brickwall_normal.jpg"),
    "specular_texture": bk.res_path("./assets/stone_bricks_gloss.jpg"),
}

plane = bk.Mesh.create_quad(3.0, bk.Alignment.XY)
plane.set_material(mat)
wall = app.add_mesh(plane)
wall.set_visible(True)


transform = Mat4.identity()


@app.event
def on_update(input, dt, t):
    global transform

    if input.is_key_pressed(bk.KeyCode.Q):
        transform = transform * Mat4.from_rotation_y(-dt * 45, degrees=True)
    if input.is_key_pressed(bk.KeyCode.E):
        transform = transform * Mat4.from_rotation_y(dt * 45, degrees=True)
    if input.is_key_pressed(bk.KeyCode.R):
        transform = transform * Mat4.from_rotation_x(dt * 45, degrees=True)
    if input.is_key_pressed(bk.KeyCode.T):
        transform = transform * Mat4.from_rotation_x(-dt * 45, degrees=True)
    if input.is_key_pressed(bk.KeyCode.F):
        transform = transform * Mat4.from_rotation_z(dt * 45, degrees=True)
    if input.is_key_pressed(bk.KeyCode.G):
        transform = transform * Mat4.from_rotation_z(-dt * 45, degrees=True)
    if input.is_key_pressed(bk.KeyCode.W):
        transform = transform * Mat4.from_translation(Vec3(0, dt, 0))
    if input.is_key_pressed(bk.KeyCode.S):
        transform = transform * Mat4.from_translation(Vec3(0, -dt, 0))
    if input.is_key_pressed(bk.KeyCode.A):
        transform = transform * Mat4.from_translation(Vec3(-dt, 0, 0))
    if input.is_key_pressed(bk.KeyCode.D):
        transform = transform * Mat4.from_translation(Vec3(dt, 0, 0))
    if input.is_key_pressed(bk.KeyCode.Z):
        transform = transform * Mat4.from_translation(Vec3(0, 0, dt))
    if input.is_key_pressed(bk.KeyCode.X):
        transform = transform * Mat4.from_translation(Vec3(0, 0, -dt))
    if input.is_key_pressed(bk.KeyCode.I):
        transform = Mat4.identity()
    wall.set_transform(transform)


app.run(win)
