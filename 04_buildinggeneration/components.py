from bk7084.math import Vec3, Mat4
from bk7084.scene import Mesh, Component
from bk7084.misc import PaletteDefault as Palette
from bk7084.scene.mesh import SubMesh


class BasicWall(Component):
    def __init__(self, w=1, h=1, texture='assets/textures/brick.jpg'):
        super().__init__()
        self._mesh = Mesh(
            vertices=[[-w / 2, 0, 0], [w / 2, 0, 0], [w / 2, h, 0], [-w / 2, h, 0]],
            colors=[Palette.BlueA.as_color()],
            normals=[[0, 0, 1]],
            uvs=[[0, 0], [1, 0], [1, 1], [0, 1]],
            triangles=[[(0, 1, 2, 3), (0, 1, 2, 3), (0, 0, 0, 0)]],
            texture=texture
        )

    @property
    def mesh(self) -> Mesh:
        return self._mesh


class Wall(Component):
    def __init__(self, w=1, h=1, texture1='assets/textures/brick.jpg', texture2='assets/textures/window.jpg'):
        super().__init__()
        self._mesh = Mesh(
            vertices=[[-w / 4, h / 4, 0], [w / 4, h / 4, 0], [w / 4, 3 * h / 4, 0], [-w / 4, 3 * h / 4, 0],
                      [-w / 2, 0, 0], [w / 2, 0, 0], [w / 2, h, 0], [-w / 2, h, 0]],
            colors=[Palette.BlueA.as_color()],
            normals=[[0, 0, 1]],
            uvs=[[0, 0], [1, 0], [1, 1], [0, 1], [0.25, 0.25], [0.75, 0.25], [0.75, 0.75], [0.25, 0.75]],
            triangles=[[(0, 1, 5, 4), (4, 5, 1, 0), (0, 0, 0, 0)],
                       [(1, 2, 6, 5), (5, 6, 2, 1), (0, 0, 0, 0)],
                       [(2, 3, 7, 6), (6, 7, 3, 2), (0, 0, 0, 0)],
                       [(3, 0, 4, 7), (7, 4, 0, 3), (0, 0, 0, 0)],
                       [(0, 1, 2, 3), (0, 1, 2, 3), (0, 0, 0, 0)]]
        )

        self._mesh.update_sub_mesh(0, SubMesh(name='wall', triangles=[0, 1, 2, 3]), texture=texture1)
        self._mesh.append_sub_mesh(SubMesh(name='window', triangles=[4]), texture=texture2)

    @property
    def mesh(self) -> Mesh:
        return self._mesh


class BasicFloor(Component):
    def __init__(self, w_x=1, w_z=1):
        super().__init__()
        self._mesh = Mesh(
            vertices=[[-w_x / 2, 0, -w_z / 2], [w_x / 2, 0, -w_z / 2],
                      [w_x / 2, 0, w_z / 2], [-w_x / 2, 0, w_z / 2]],
            colors=[Palette.RedA.as_color()],
            normals=[[0, 1, 0]],
            uvs=[[0, 0], [1, 0], [1, 1], [0, 1]],
            triangles=[[(0, 1, 2, 3), (0, 1, 2, 3), (0, 0, 0, 0)]],
        )
    
    @property
    def mesh(self) -> Mesh:
        return self._mesh


class Ground(Component):
    def __init__(self, y=-0.01, w=20, repeat_texture=8, texture='assets/textures/grass.jpg'):
        super().__init__()
        self._mesh = Mesh(
            vertices=[[-w / 2, y, -w / 2], [w / 2, y, -w / 2],
                      [w / 2, y, w / 2], [-w / 2, y, w / 2]],
            colors=[Palette.GreenA.as_color()],
            normals=[[0, 1, 0]],
            uvs=[[0, 0], [repeat_texture, 0], [repeat_texture, repeat_texture], [0, repeat_texture]],
            triangles=[[(0, 1, 2, 3), (0, 1, 2, 3), (0, 0, 0, 0)]],
            texture=texture
        )
    
    @property
    def mesh(self) -> Mesh:
        return self._mesh
