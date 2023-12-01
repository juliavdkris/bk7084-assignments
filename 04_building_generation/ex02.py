import bk7084 as bk
import numpy as np
from bk7084.math import *

# Sub meshes

win = bk.Window()
win.set_title("BK7084 - Lab 4 - Building Generation [ex02]")
win.set_size(800, 800)
win.set_resizable(True)

app = bk.App()
camera = app.create_camera(pos=Vec3(2, 0, 8), look_at=Vec3(0, 0, 0), fov_v=60.0, background=bk.Color.ICE_BLUE)
camera.set_as_main_camera()

light = app.add_point_light(Vec3(0, 0, 5.2), bk.Color(0.8, 0.8, 0.8), show_light=False)

wall_mesh = bk.Mesh()
wall_mesh.vertices = np.array([
    [-0.5, -0.5, 0.0], [0.5, -0.5, 0.0], [0.5, 0.5, 0.0], [-0.5, 0.5, 0.0],
    [-0.2, -0.2, 0.0], [0.2, -0.2, 0.0], [0.2, 0.2, 0.0], [-0.2, 0.2, 0.0],
    [-0.2, -0.2, 0.0], [0.2, -0.2, 0.0], [0.2, 0.2, 0.0], [-0.2, 0.2, 0.0],
]) * 8.0
wall_mesh.uvs = [[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0, 1.0],
                 [0.3, 0.3], [0.7, 0.3], [0.7, 0.7], [0.3, 0.7],
                 [0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0, 1.0]
                 ]
wall_mesh.triangles = [
    [0, 1, 5], [0, 5, 4], [1, 2, 6], [1, 6, 5], [2, 3, 7], [2, 7, 6], [3, 0, 4], [3, 4, 7],  # outter wall
    [8, 9, 10], [8, 10, 11],  # inner wall
]

mat_inner = bk.Material()
mat_inner.textures = {
    "diffuse_texture": bk.res_path("../03_textures/assets/stone_bricks_col.jpg"),
    "normal_texture": bk.res_path("../03_textures/assets/stone_bricks_nrm.png"),
    "specular_texture": bk.res_path("../03_textures/assets/stone_bricks_refl.jpg"),
    "shininess_texture": bk.res_path("../03_textures/assets/stone_bricks_gloss.jpg"),
}

mat_outer = bk.Material()
mat_outer.textures = {
    "diffuse_texture": bk.res_path("../03_textures/assets/mosaic_tiles_col.png"),
    "normal_texture": bk.res_path("../03_textures/assets/mosaic_tiles_nrm.png"),
    "specular_texture": bk.res_path("../03_textures/assets/mosaic_tiles_refl.png"),
    "shininess_texture": bk.res_path("../03_textures/assets/mosaic_tiles_gloss.png"),
}

wall_mesh.materials = [mat_inner, mat_outer]
wall_mesh.sub_meshes = [
    bk.SubMesh(0, 24, 0),
    bk.SubMesh(24, 30, 1),
]

wall = app.add_mesh(wall_mesh)
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
    if input.is_key_pressed(bk.KeyCode.P):
        is_plane = True
    if input.is_key_pressed(bk.KeyCode.L):
        is_plane = False

    wall.set_transform(transform)


app.run(win)

