
import os.path as osp
import bk7084 as bk
from bk7084.math import *
import numpy as np

# Setup window and add camera
window = bk.Window()
window.set_title('BK7084 - Lab 1 - Transformation [bonus]')
window.set_size(1024, 1024)
window.set_resizable(True)

app = bk.App()

camera = app.create_camera(Vec3(0, 0.0, 10.0), Vec3(0, 0, 0), 60.0)

# Create a grid
# grid = Grid(20, 20, 1.0, 1.0, axis_alignment=AxisAlignment.XY)

# Create a triangle and ray and set the animation flag
triangle = app.add_mesh(bk.Mesh.create_triangle(Vec(-2, -2, 1), Vec(2, -2, 1), Vec(0, 2, 1)))

# ray = Ray([0, -3, 2], [4, 4, 1])
animate = True

"""
Assignment 1: Intersection
--------------------------

Please read the accompanying PDF file for an explanation of this assignment.

Your tasks:
1. Build mat_A, vec_b of the linear system.
2. Solve the linear system with NumPy's np.linalg.solve(A, b).
3. Implement the intersection conditions based on the solution.
"""
def intersect_ray_triangle(ray, tri):
    mat_A = Mat3()      # 1. Set up matrix A
    vec_b = Vec3()      # 1. Set up vector b
    vec_x = None        # 2. Solve the linear system

    return False        # 3. Implement the intersection conditions based on the solution
"""
If you have implemented everything correctly,
you should see the triangle turn red when it's intersected by the ray.
"""

@window.event
def on_draw(dt):
    draw(triangle, grid, ray)


@window.event
def on_key_press(key, mods):
    global animate
    if key == KeyCode.A:
        animate = not animate


@window.event
def on_update(dt):
    if animate:
        ray.direction = Mat3.from_rotation_y(dt * 90.0, True) * ray.direction
    if intersect_ray_triangle(ray, triangle):
        triangle.color = PaletteDefault.RedA.as_color()
    else:
        triangle.color = PaletteSvg.SkyBlue.as_color()


app.run(window)
