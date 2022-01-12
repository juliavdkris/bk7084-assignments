from bk7084.scene import Mesh, Component, Entity, Building
from bk7084.misc import PaletteDefault as Palette
from bk7084.scene.mesh import SubMesh


"""
TODO Add your own components here, following the examples given below.
"""

class BasicWall(Component):
    """A basic wall component that is centered horizontally at (0, 0, 0)
    and aligned to the x-axis with it's bottom edge:
    
    (-w/2, h, 0)  ___  (w/2, h, 0)
                 |   |
                 |___|
    (-w/2, 0, 0)   ^   (w/2, 0, 0)
               (0, 0, 0)

    You can use this component as a template for new components.

    Args:
        w (float):
            Width of the wall component.
        h (float):
            Height of the wall component.
        texture (str):
            Path to the texture used for this component.
    """
    def __init__(self, w=1, h=1, texture='assets/textures/brick.jpg'):
        """You can create a mesh in the __init__ class and store it in self._mesh.
        Other classes can access this attribute with the mesh property below.
        Make sure that any new component you make also contains the mesh property.
        """
        super().__init__()
        # You can create a mesh 'from scratch' by defining the vertices
        # and triangles (faces) yourself.
        self._mesh = Mesh(
            # These are the four corners of the wall
            vertices=[[-w / 2, 0, 0], [w / 2, 0, 0], [w / 2, h, 0], [-w / 2, h, 0]],
            # You can give a list of colors for each vertex.
            # Here, we use the same color for each vertex and therefore only add one color to the list.
            colors=[Palette.BlueA.as_color()],
            # We also provide a normal for each vertex. The normal points away from the surface.
            # Therefore, we set the normal to point into the z-axis.
            # We use the same normal for each vertex, so we'll only add one normal to the list of normals.
            normals=[[0, 0, 1]],
            # UV coordinates refer to a location in the texture and should be given for each vertex.
            # In UV coordinates, the texture's bottom-left corner is at (0, 0) and the top-right corner at (1, 1).
            # That means you don't have to think about the actual resolution of the texture when you define UV-coordinates.
            uvs=[[0, 0], [1, 0], [1, 1], [0, 1]],
            # Finally, we can start defining the triangles (or faces)
            # and set the uv-coordinates and normals belonging to each vertex.
            #           Vertex indices  UV indices     Normal indices
            triangles=[[(0, 1, 2, 3),   (0, 1, 2, 3),  (0, 0, 0, 0)]],
            # And we set the texture of this mesh to the file path that we give to the __init__ function.
            texture=texture
        )

    @property
    def mesh(self) -> Mesh:
        """This is the mesh property that other code uses to get access to the mesh.
        If you want, you can also add functionality here,
        but it suffices to just return self._mesh
        """
        return self._mesh


class WindowWall(Component):
    """An advanced wall component that is centered horizontally at (0, 0, 0)
    and aligned to the x-axis with it's bottom edge.
    This wall has a separate Window texture in the center.

    The wall is constructed with 5 faces:
                
    (-w/2, h, 0) _______ (w/2, h, 0)
                | \ _ / |
                |  |_|  |
                |_/___\_|
    (-w/2, 0, 0)    ^    (w/2, 0, 0)
                (0, 0, 0)

    These faces each have four vertices: they're quadrilaterals (quads), not triangles.
    The Mesh class takes care of breaking up faces with more vertices into triangles.

    The triangles are given two different textures using a SubMesh.
    The four faces on the edge are part of one submesh, the center face is the other submesh.

    Args:
        w (float):
            Width of the wall component.
        h (float):
            Height of the wall component.
        wall_texture (str):
            Path to the texture used for this the wall.
        window_texture (str):
            Path to the texture used for the window.
    """
    def __init__(self, w=1, h=1, wall_texture='assets/textures/brick.jpg', window_texture='assets/textures/window.jpg'):
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

        # These submeshes can be used to apply different materials to parts of the mesh
        # Provide the SubMesh with a name the indices of the triangles part of the submesh
        # and the path of the texture for this SubMesh.
        self._mesh.update_sub_mesh(0, SubMesh(name='wall', triangles=[0, 1, 2, 3]), texture=wall_texture)
        self._mesh.append_sub_mesh(SubMesh(name='window', triangles=[4]), texture=window_texture)

    @property
    def mesh(self) -> Mesh:
        return self._mesh


class BasicFloor(Component):
    """A basic floor component that aligns with the xz-plane.
    
    Args:
        w_x (float):
            Width of the floor component in the x-direction.
        w_z (float):
            Width of the floor component in the z-direction.
        texture (str):
            Path to the texture used for this component.
    """
    def __init__(self, w_x=1, w_z=1, texture=None):
        super().__init__()
        self._mesh = Mesh(
            vertices=[[-w_x / 2, 0, -w_z / 2], [w_x / 2, 0, -w_z / 2],
                      [w_x / 2, 0, w_z / 2], [-w_x / 2, 0, w_z / 2]],
            colors=[Palette.RedA.as_color()],
            normals=[[0, 1, 0]],
            uvs=[[0, 0], [1, 0], [1, 1], [0, 1]],
            triangles=[[(0, 1, 2, 3), (0, 1, 2, 3), (0, 0, 0, 0)]],
            texture=texture
        )
        self._mesh.material_enabled = False
    
    @property
    def mesh(self) -> Mesh:
        return self._mesh
