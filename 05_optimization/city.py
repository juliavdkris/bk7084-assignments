from enum import Enum

from bk7084.math import Vec3, Mat4
from bk7084.graphics import draw
from bk7084.geometry import Grid as GridLine
from bk7084.scene import Mesh, Component, Entity, Building
from bk7084.misc import PaletteDefault as Palette

from buildings import *


class PlotType(Enum):
    EMPTY = 0
    PARK = 1
    HOUSE = 2
    OFFICE = 3
    HIGHRISE = 4
    SKYSCRAPER = 5


class City(Entity):
    def __init__(self, name='GridCity', cell_size=(2.0, 2.0), row=8, col=8):
        super().__init__(name)
        self._is_drawable = True
        self._row = row
        self._col = col
        self._grid = Grid(cell_size=cell_size, row=self._row, col=self._col)
        self._plots = [PlotType.EMPTY] * row * col

        """
        Change the building for each plottype to your own buildings, e.g.:
        >>> PlotType.OFFICE: Skyscraper(3, 1).convert_to_mesh(),
        >>> PlotType.HIGHRISE: Skyscraper(4, 1).convert_to_mesh(),
        """
        self._buildings = {
            PlotType.EMPTY: None,
            PlotType.PARK: Mesh('assets/meshes/Park.obj', texture_enabled=False),
            PlotType.HOUSE: Mesh('assets/meshes/House.obj', texture_enabled=False),
            PlotType.OFFICE: Office(2, 1).convert_to_mesh(),
            PlotType.HIGHRISE: Highrise(3, 1).convert_to_mesh(),
            PlotType.SKYSCRAPER: Skyscraper(5, 1).convert_to_mesh()
        }
        
        """
        Each plot is initialized here.
        You can change this code to initialize your city in a different layout.
        """
        self.set_plot_type(0, 0, PlotType.SKYSCRAPER)
        self.set_plot_type(0, 1, PlotType.SKYSCRAPER)
        self.set_plot_type(1, 0, PlotType.HOUSE)
        self.set_plot_type(1, 1, PlotType.HOUSE)
        self.set_plot_type(2, 0, PlotType.PARK)
        self.set_plot_type(2, 1, PlotType.PARK)

    @property
    def row(self):
        return self._row

    @property
    def col(self):
        return self._col

    def get_building(self, type):
        return self._buildings[type]      

    def get_plot_type(self, i, j):
        return self._plots[i * self._col + j]

    def set_plot_type(self, i, j, type):
        self._plots[i * self._col + j] = type

    def swap(self, i, j, k, l):
        temp = self.get_plot_type(i, j)
        self.set_plot_type(i, j, self.get_plot_type(k, l))
        self.set_plot_type(k, l, temp)

    def draw(self, shader=None, **kwargs):
        self._grid.draw(**kwargs)
        for i in range(self.row):
            for j in range(self.col):
                type = self.get_plot_type(i, j)
                if type != PlotType.EMPTY:
                    building = self.get_building(type)
                    building.transformation = Mat4.from_translation(self._grid.cell_position(i, j))
                    building.draw(shader=shader, **kwargs)

    @property
    def meshes(self):
        meshes = []
        meshes += self._grid.meshes
        for i in range(self.row):
            for j in range(self.col):
                type = self.get_plot_type(i, j)
                if type != PlotType.EMPTY:
                    mesh = self.get_building(type)
                    transform = Mat4.from_translation(self._grid.cell_position(i, j))
                    meshes.append((mesh, transform))
        return meshes




class Grid(Building):
    """ A ground plane with a grass texture and optional grid tiling.
    
    Args:
        y (float):
            Location of the grid plane on the y-axis.
        cell_size ((float, float)):
            Width and height of the grid cell.
        row (int):
            Number of rows of the grid.
        col (int):
            Number of rows of the grid.
        grid_enabled (bool):
            Draws a grid of lines is set to True.
    """
    def __init__(self, y=-0.01, cell_size=(2.0, 2.0), row=8, col=8, grid_enabled=True):
        super().__init__(name='Grid')
        self._y = y
        self._cell_size = cell_size
        self._row = row
        self._col = col
        self._w = col * cell_size[0]
        self._h = row * cell_size[1]
        self._grid_enabled = grid_enabled
        self._grid = GridLine(width=self._w, height=self._h, spacing_width=2.0, spacing_height=2.0)

        # per row then per column
        for i in range(row):
            for j in range(col):
                cell = GridCell(cell_size[0], cell_size[1], PlotType.EMPTY)
                cell.transform = Mat4.from_translation(self.cell_position(i, j))
                self.append(cell)

    def cell_position(self, i, j):
        return Vec3(
                    -self._w / 2 + self._cell_size[0] / 2.0 + self._cell_size[0] * j,
                    self._y,
                    -self._h / 2 + self._cell_size[1] / 2.0 + self._cell_size[1] * i
                )

    def draw(self, **kwargs):
        super().draw(**kwargs)
        if self._grid_enabled:
            draw(self._grid, transform=Mat4.from_translation(Vec3(0.0, self._y + 0.01, 0.0)))


class GridCell(Component):
    """A cell in the grid.

    Args:
        w(float):
            Width of the ground cell.

        h(float):
            Height of the ground cell.

        kind (GroundCellKind):
            Type of the ground cell.

        texture (str):
            Path to the texture of this ground cell.
    """
    def __init__(self, w=1.0, h=1.0, type=PlotType.EMPTY, texture='assets/textures/grass.jpg'):
        super(GridCell, self).__init__()
        self._type = type
        self._mesh = Mesh(
            vertices=[[-w / 2, 0, -h / 2], [w / 2, 0, -h / 2],
                      [w / 2, 0, h / 2], [-w / 2, 0, h / 2]],
            colors=[Palette.RedA.as_color()],
            normals=[[0, 1, 0]],
            uvs=[[0, 0], [1, 0], [1, 1], [0, 1]],
            triangles=[[(0, 1, 2, 3), (0, 1, 2, 3), (0, 0, 0, 0)]],
            texture=texture
        )

    @property
    def mesh(self) -> Mesh:
        return self._mesh

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value: PlotType):
        self._type = value


