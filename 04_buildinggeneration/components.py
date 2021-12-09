from bk7084.math import Vec3, Mat4
from bk7084.scene import Mesh, Component
from bk7084.misc import PaletteDefault as Palette
from bk7084.scene.mesh import SubMesh


class Wall(Component):
    def __init__(self, w, h, texture1, texture2):
        super().__init__()
        self._mesh = Mesh(
            vertices=[[-w / 2.0, -h / 2.0, 0.0], [w / 2.0, -h / 2.0, 0.0], [w / 2.0, h / 2.0, 0.0], [-w / 2.0, h / 2.0, 0.0],
                      [-w, -h, 0.0], [w, -h, 0.0], [w, h, 0.0], [-w, h, 0.0]],
            colors=[Palette.BlueA.as_color()],
            normals=[[0.0, 0.0, 1.0]],
            uvs=[[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.25, 0.25], [0.75, 0.25], [0.75, 0.75], [0.25, 0.75]],
            triangles=[[(0, 1, 5, 4), (4, 5, 1, 0), (0, 0, 0, 0)],
                       [(1, 2, 6, 5), (5, 6, 2, 1), (0, 0, 0, 0)],
                       [(2, 3, 7, 6), (6, 7, 3, 2), (0, 0, 0, 0)],
                       [(3, 0, 4, 7), (7, 4, 0, 3), (0, 0, 0, 0)],
                       [(0, 1, 2, 3), (0, 1, 2, 3), (0, 0, 0, 0)]])

        self._mesh.update_sub_mesh(0, SubMesh(name='body', triangles=[0, 1, 2, 3]), texture=texture1)
        self._mesh.append_sub_mesh(SubMesh(name='window', triangles=[4]), texture=texture2)
        self._mesh.texture_enabled = True
        self._mesh.apply_transformation(Mat4.from_rotation_y(45, True))

    @property
    def mesh(self) -> Mesh:
        return self._mesh