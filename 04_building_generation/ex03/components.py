import bk7084 as bk
import numpy as np
from numpy.random import randint, rand

"""
Materials are used to define the appearance of a mesh.
"""
material_stone_bricks = bk.Material()
material_stone_bricks.textures = {
    "diffuse_texture": bk.res_path("../03_textures/assets/stone_bricks_col.jpg"),
    "normal_texture": bk.res_path("../03_textures/assets/stone_bricks_nrm.png"),
    "specular_texture": bk.res_path("../03_textures/assets/stone_bricks_refl.jpg"),
    "shininess_texture": bk.res_path("../03_textures/assets/stone_bricks_gloss.jpg"),
}

material_basic_bricks = bk.Material()
material_basic_bricks.specular = bk.Color(0.1, 0.1, 0.1)
material_basic_bricks.textures = {
    "diffuse_texture": bk.res_path("../assets/brick.jpg"),
}

material_basic_floor = bk.Material()
material_basic_floor.diffuse = bk.Color(0.8, 0.5, 0.5)

material_basic_window = bk.Material()
material_basic_window.textures = {
    "diffuse_texture": bk.res_path("../assets/window.jpg"),
}

material_basic_ground = bk.Material()
material_basic_ground.textures = {
    "diffuse_texture": bk.res_path("../assets/grass.jpg"),
}


def create_basic_wall(w=1, h=1, m=material_basic_bricks):
    """
    Create a basic wall mesh with the given size and material.
    Args:
        w: the width of the wall
        h: the height of the wall
        m (bk.Material): the material of the wall

    Returns:
        A bk.Mesh object representing the wall.
    """
    # If the mesh is not created, create it.
    if not hasattr(create_basic_wall, "mesh"):
        create_basic_wall.mesh = bk.Mesh()
        create_basic_wall.mesh.name = "BasicWallMesh"
        create_basic_wall.mesh.positions = np.array([[-w, -h, 0], [w, -h, 0], [w, h, 0], [-w, h, 0]]) * 0.5
        create_basic_wall.mesh.texcoords = [[0, 0], [1, 0], [1, 1], [0, 1]]
        create_basic_wall.mesh.triangles = [[0, 1, 2], [0, 2, 3]]
    if m is not None:
        create_basic_wall.mesh.materials = [m]
    # If the mesh is created, just return it.
    return create_basic_wall.mesh


class BasicWall(bk.Mesh):
    """
    Create a basic wall mesh with the given size and material.
    This class is a subclass of bk.Mesh, so it can be used as a mesh. For example,
    you can create a mesh instance by `mesh = BasicWallMesh(...)`, and then add it to
    a scene by `app.add_mesh(mesh)`. It's the same as using `mesh = create_basic_wall(...)`.
    """

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, w=1, h=1, m=material_basic_bricks):
        super().__init__()
        self.w = w
        self.h = h
        self.name = "BasicWallMesh"
        self.positions = [
            [-w / 2, -h / 2, 0],
            [w / 2, -h / 2, 0],
            [w / 2, h / 2, 0],
            [-w / 2, h / 2, 0],
        ]
        self.texcoords = [[0, 0], [1, 0], [1, 1], [0, 1]]
        self.triangles = [[0, 1, 2], [0, 2, 3]]
        self.materials = [m]


def create_basic_floor(w=1, h=1, m=material_basic_floor):
    """
    Create a basic floor mesh with the given size and material.
    The floor is aligned with the xz-plane.

    Args:
        w: the width of the floor
        h: the height of the floor
        m (bk.Material): the material of the floor

    Returns:
        A bk.Mesh object representing the floor.
    """
    # If the mesh is not created, create it.
    # In Python, functions are objects, so we can add attributes to functions.
    # `hasattr` checks if the function has an attribute with the given name.
    # The reason we use hasattr is to make sure the mesh is created only once.
    # We don't want to create the same mesh multiple times.
    if not hasattr(create_basic_floor, "mesh"):
        create_basic_floor.mesh = bk.Mesh()
        create_basic_floor.mesh.name = "BasicFloorMesh"
        create_basic_floor.mesh.positions = np.array([
            [-w / 2, 0, -h / 2],
            [w / 2, 0, -h / 2],
            [w / 2, 0, h / 2],
            [-w / 2, 0, h / 2],
        ])
        create_basic_floor.mesh.texcoords = [[0, 0], [1, 0], [1, 1], [0, 1]]
        create_basic_floor.mesh.triangles = [[0, 2, 1], [0, 3, 2]]
    if m is not None:
        create_basic_floor.mesh.materials = [m]
    # If the mesh is created, just return it.
    return create_basic_floor.mesh


class BasicFloor(bk.Mesh):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, w=1, h=1, m=material_basic_floor):
        super().__init__()
        self.w = w
        self.h = h
        self.name = "BasicFloorMesh"
        # self.materials = materials
        self.positions = [
            [-w / 2, 0, -h / 2],
            [w / 2, 0, -h / 2],
            [w / 2, 0, h / 2],
            [-w / 2, 0, h / 2],
        ]
        self.texcoords = [[0, 0], [1, 0], [1, 1], [0, 1]]
        self.triangles = [[0, 2, 1], [0, 3, 2]]
        self.materials = [m]


def create_basic_window_wall(w=1, h=1):
    """
    Create a window wall mesh with the given size and material.

    Args:
        w: the width of the wall
        h: the height of the wall

    Returns:
        A bk.Mesh object representing the wall.
    """
    # If the mesh is not created, create it.
    if not hasattr(create_basic_window_wall, "mesh"):
        create_basic_window_wall.mesh = bk.Mesh()
        create_basic_window_wall.mesh.name = "BasicWindowWallMesh"
        create_basic_window_wall.mesh.positions = [
            [-w/2, -h/2, 0.0], [w/2, -h/2, 0.0], [w/2, h/2, 0.0], [-w/2, h/2, 0.0],
            [-w*0.2, -h*0.2, 0.0], [w*0.2, -h*0.2, 0.0], [w*0.2, h*0.2, 0.0], [-w*0.2, h*0.2, 0.0],
            [-w*0.2, -h*0.2, 0.0], [w*0.2, -h*0.2, 0.0], [w*0.2, h*0.2, 0.0], [-w*0.2, h*0.2, 0.0],
        ]
        create_basic_window_wall.mesh.texcoords = [
            [0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0, 1.0],
            [0.3, 0.3], [0.7, 0.3], [0.7, 0.7], [0.3, 0.7],
            [0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0, 1.0]
        ]
        create_basic_window_wall.mesh.triangles = [
            [0, 1, 5], [0, 5, 4], [1, 2, 6], [1, 6, 5], [2, 3, 7], [2, 7, 6], [3, 0, 4], [3, 4, 7],
            [8, 9, 10], [8, 10, 11],
        ]
        create_basic_window_wall.mesh.materials = [
            material_basic_bricks,
            material_basic_window,
        ]
        create_basic_window_wall.mesh.sub_meshes = [
            bk.SubMesh(0, 8, 0),
            bk.SubMesh(8, 10, 1),
        ]
    # If the mesh is created, just return it.
    return create_basic_window_wall.mesh


class BasicWindowWall(bk.Mesh):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, w=1, h=1):
        super().__init__()
        self.w = w
        self.h = h
        self.name = "BasicWindowWallMesh"
        # self.materials = materials
        self.positions = [
            [-w/2, -h/2, 0.0], [w/2, -h/2, 0.0], [w/2, h/2, 0.0], [-w/2, h/2, 0.0],
            [-w*0.2, -h*0.2, 0.0], [w*0.2, -h*0.2, 0.0], [w*0.2, h*0.2, 0.0], [-w*0.2, h*0.2, 0.0],
            [-w*0.2, -h*0.2, 0.0], [w*0.2, -h*0.2, 0.0], [w*0.2, h*0.2, 0.0], [-w*0.2, h*0.2, 0.0],
        ]
        self.texcoords = [
            [0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0, 1.0],
            [0.3, 0.3], [0.7, 0.3], [0.7, 0.7], [0.3, 0.7],
            [0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0, 1.0]
        ]
        self.triangles = [
            [0, 1, 5], [0, 5, 4], [1, 2, 6], [1, 6, 5], [2, 3, 7], [2, 7, 6], [3, 0, 4], [3, 4, 7],
            [8, 9, 10], [8, 10, 11],
        ]
        self.materials = [
            material_basic_bricks,
            material_basic_window,
        ]
        self.sub_meshes = [
            bk.SubMesh(0, 8, 0),
            bk.SubMesh(8, 10, 1),
        ]
