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


class City(object):
    def __init__(self, cell_size=(2.0, 2.0), row=8, col=8):
        self._row = row
        self._col = col
        self._mincorner = Vec3()

        self._grid = Grid(row=self._row, col=self._col)
        
        self._plots = [[PlotType.EMPTY] * col] * row
        
        """
        Initialize your city here
        """
        self.set_plot_type(0, 6, PlotType.SKYSCRAPER)
        self.set_plot_type(0, 7, PlotType.SKYSCRAPER)
        self.set_plot_type(1, 6, PlotType.SKYSCRAPER)
        self.set_plot_type(1, 7, PlotType.SKYSCRAPER)
        self.set_plot_type(2, 6, PlotType.SKYSCRAPER)
        self.set_plot_type(2, 7, PlotType.SKYSCRAPER)

        # 18 offices
        for i in range(6):
            self.set_plot_type(0, i, PlotType.OFFICE)
            self.set_plot_type(1, i, PlotType.OFFICE)
            self.set_plot_type(2, i, PlotType.OFFICE)

        # 10 highrises
        for i in range(5):
            self.set_plot_type(6, i, PlotType.HIGHRISE)
            self.set_plot_type(7, i, PlotType.HIGHRISE)
        
        self.set_plot_type(6, 5, PlotType.HOUSE)
        self.set_plot_type(7, 5, PlotType.HOUSE)
        
        # 26 residencial blocks
        for i in range(8):        
            self.set_plot_type(3, i, PlotType.HOUSE)
            self.set_plot_type(4, i, PlotType.HOUSE)
            self.set_plot_type(5, i, PlotType.HOUSE)            
        
        # 4 parks
        self.set_plot_type(6, 6, PlotType.PARK)
        self.set_plot_type(6, 7, PlotType.PARK)
        self.set_plot_type(7, 6, PlotType.PARK)
        self.set_plot_type(7, 7, PlotType.PARK)

    def get_building(self, type):
        if type == PlotType.EMPTY:
            return None
        elif type == PlotType.PARK:
            return Skyscraper(1, 1)
        elif type == PlotType.HOUSE:
            return Skyscraper(2, 1)
        elif type == PlotType.OFFICE:
            return Skyscraper(3, 1)
        elif type == PlotType.HIGHRISE:
            return Skyscraper(4, 1)
        elif type == PlotType.SKYSCRAPER:
            return Skyscraper(5, 1)
        else:
            return Skyscraper(1, 1)

    def get_plot_type(self, i, j):
        return self._plots[i][j]

    def set_plot_type(self, i, j, type):
        self._plots[i][j] = type

    def swap(self, i, j, k, l):
        temp = self.get_plot_type(i, j)
        self.set_plot_type(i, j, self.get_plot_type(k, l))
        self.set_plot_type(k, l, temp)

    @property
    def buildings(self):
        buildings = [self._grid]
        for i in range(self._row):
            for j in range(self._col):
                type = self.get_plot_type(i, j)
                if type != PlotType.EMPTY:
                    building = self.get_building(type)
                    building.transform = Mat4.from_translation(self._grid.cell_position(i, j))
                    buildings.append(building)
        return buildings


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


