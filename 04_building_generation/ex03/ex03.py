import bk7084 as bk
import numpy as np
from bk7084.math import *


stone_brick_material = bk.Material()
stone_brick_material.textures = {
    "diffuse_texture": bk.res_path("../../03_textures/assets/stone_bricks_col.jpg"),
    "normal_texture": bk.res_path("../../03_textures/assets/stone_bricks_nrm.png"),
    "specular_texture": bk.res_path("../../03_textures/assets/stone_bricks_refl.jpg"),
    "shininess_texture": bk.res_path("../../03_textures/assets/stone_bricks_gloss.jpg"),
}


# Mesh construction
def create_basic_wall(width: float, height: float, materials: list = None):
    create_basic_wall._mesh = bk.Mesh()
    create_basic_wall._mesh.vertices = np.array(
        [
            [-width / 2, -height / 2, 0],
            [width / 2, -height / 2, 0],
            [width / 2, height / 2, 0],
            [-width / 2, height / 2, 0],
        ]
    )
    create_basic_wall._mesh.uvs = [[0, 0], [1, 0], [1, 1], [0, 1]]
    create_basic_wall._mesh.triangles = [[0, 1, 2], [0, 2, 3]]
    create_basic_wall._mesh.materials = materials
    return create_basic_wall._mesh


win = bk.Window()
win.set_title("BK7084 - Lab 4 - Building Generation [ex03]")
win.set_size(800, 800)
win.set_resizable(True)

app = bk.App()
camera = app.create_camera(
    pos=Vec3(2, 0, 8), look_at=Vec3(0, 0, 0), fov_v=60.0, background=bk.Color.ICE_BLUE
)
camera.set_as_main_camera()

light = app.add_point_light(Vec3(0, 0, 5.2), bk.Color(0.8, 0.8, 0.8), show_light=False)

wall_mesh = create_basic_wall(5, 5, [stone_brick_material])

for i in range(4):
    wall = app.add_mesh(wall_mesh)
    wall.set_transform(
        Mat4.from_rotation_y(i * 90, degrees=True)
        * Mat4.from_translation(Vec3(0, 0, 2.5))
    )
    wall.set_visible(True)


# house = app.create_building()
# house.add_wall(wall0)

# wall0.set_transform(Mat4.from_translation(Vec3(-2, 0, 0)))

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
    if input.is_key_pressed(bk.KeyCode.P):
        is_plane = True
    if input.is_key_pressed(bk.KeyCode.L):
        is_plane = False

    # wall.set_transform(transform)


app.run(win)
