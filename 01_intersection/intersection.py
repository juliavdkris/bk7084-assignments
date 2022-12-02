
import numpy as np
from bk7084 import Window, app
from bk7084.app.input import KeyCode
from bk7084.geometry import Triangle, Ray, Grid, AxisAlignment
from bk7084.math import Vec3, Mat3
from bk7084.misc import PaletteSvg, PaletteDefault
from bk7084.graphics import draw

# Setup window and add camera
window = Window("BK7084: 01-Intersection")
window.create_camera(Vec3(0, 0.0, 10.0), Vec3(0, 0, 0), Vec3.unit_y(), 60.0)

# Create a grid
grid = Grid(20, 20, 1.0, 1.0, axis_alignment=AxisAlignment.XY)

# Create a triangle and ray and set the animation flag
triangle = Triangle([-2, -2, 1], [2, -2, 1], [0, 2, 1])
ray = Ray([0, -3, 2], [4, 4, 1])
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
    """
    You can get the three vertices of the triangle as follows:
    >>> a = tri.p0
    >>> b = tri.p1
    >>> c = tri.p2
    You can get the direction and origin of the ray as follows:
    >>> direction = ray.direction
    >>> origin = ray.origin
    You can get the x, y, z coordinate of a vector as follows:
    >>> x_coord = a.x
    >>> y_coord = a.y
    >>> z_coord = a.z
    """
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


app.init(window)
app.run()
