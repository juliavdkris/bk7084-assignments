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
        """ A city class that places buildings in a grid.
        
        Args:
            name (str): The name of the city. Used for printing the city.
            cell_size (tuple): The size of each grid cell.
            row (int): The number of rows in the grid.
            col (int): The number of columns in the grid.
        """
        super().__init__(name)
        self._is_drawable = True
        self._row = row
        self._col = col
        self._grid = Grid(cell_size=cell_size, row=self._row, col=self._col)
        self._plots = []

        """ You can change the building that is placed on each plot here.
        """
        self._buildings = {
            PlotType.EMPTY: None,
            PlotType.PARK: Mesh('assets/meshes/Park.obj', texture_enabled=False),
            PlotType.HOUSE: Mesh('assets/meshes/House.obj', texture_enabled=False),
            PlotType.OFFICE: Office(2, 1).convert_to_mesh(),
            PlotType.HIGHRISE: Highrise(3, 1).convert_to_mesh(),
            PlotType.SKYSCRAPER: Skyscraper(5, 1).convert_to_mesh()
        }
        self.reset()
    
        print(self)

    def reset(self):
        """ Resets the city to its initial state.
        Complete this method to initialize your city to match the required specification:
            6 Skyscrapers of roughly
            10 High rises of roughly
            18 Offices (or your choice of building)
            26 Houses
            4 Parks
        """
        # TODO: Initialize the city grid in a smart way.
        self.clear()
        self.set_plot_type(0, 0, PlotType.HOUSE)
        self.set_plot_type(0, 1, PlotType.HOUSE)
        self.set_plot_type(1, 0, PlotType.OFFICE)
        self.set_plot_type(1, 1, PlotType.OFFICE)
        self.set_plot_type(2, 0, PlotType.HIGHRISE)
        self.set_plot_type(2, 1, PlotType.HIGHRISE)
        self.set_plot_type(3, 0, PlotType.SKYSCRAPER)
        self.set_plot_type(3, 1, PlotType.SKYSCRAPER)
        self.set_plot_type(4, 0, PlotType.PARK)
        self.set_plot_type(4, 1, PlotType.PARK)

    def clear(self):
        """ Fills the grid with empty plots.
        """
        self._plots = [PlotType.EMPTY] * self.row * self.col

    @property
    def row(self):
        return self._row

    @property
    def col(self):
        return self._col

    @property
    def grid(self):
        return self._grid   

    def get_plot_type(self, i, j):
        """ Returns the plot type of a given grid cell.
        
        Args:
            i (int): The row-index of the grid cell.
            j (int): The column-index of the grid cell.
        """
        return self._plots[i * self.col + j]

    def set_plot_type(self, i, j, type):
        """ Sets the plot type of a given grid cell.

        Args:
            i (int): The row-index of the grid cell.
            j (int): The column-index of the grid cell.
            type (PlotType): The type to set for this grid cell, e.g. PlotType.HOUSE.
        """
        self._plots[i * self.col + j] = type

    def swap(self, i_a, j_a, i_b, j_b):
        """ Swaps the plot type of two grid cells, (i, j) and (k, l).

        Args:
            i_a (int): The row-index of the first grid cell.
            j_a (int): The column-index of the first grid cell.
            i_b (int): The row-index of the second grid cell.
            j_b (int): The column-index of the second grid cell.
        """
        temp = self.get_plot_type(i_a, j_a)
        self.set_plot_type(i_a, j_a, self.get_plot_type(i_b, j_b))
        self.set_plot_type(i_b, j_b, temp)

    def get_building(self, type):
        """ Returns the building instance for a given plot type.
        
        Args:
            type (PlotType): Defines the type of this plot, e.g., PlotType.HOUSE.
        """
        return self._buildings[type]   

    def draw(self, shader=None, **kwargs):
        """
        Draws the city to screen.
        """
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
        """ Returns all the meshes in the city and their corresponding transforms.
        """
        meshes = []
        meshes += self._grid.meshes
        for i in range(self.row):
            for j in range(self.col):
                type = self.get_plot_type(i, j)
                if type != PlotType.EMPTY:
                    mesh = self.get_building(type)
                    transform = Mat4.from_translation(self._grid.cell_position(i, j))
                    if mesh:
                        meshes.append((mesh, transform))
        return meshes

    def building_at(self, i, j):
        """ Returns the mesh of the building for a given grid cell.
        """
        plot_type = self.get_plot_type(i, j)
        mesh = self.get_building(plot_type)
        transform = Mat4.from_translation(self.grid.cell_position(i, j))
        return mesh, transform

    def __repr__(self):
        repr_string = self.name + '\n'
        for i in range(self.row):
            for j in range(self.col):
                repr_string += str(self.get_plot_type(i, j).name)[:4] + '\t'
            repr_string += '\n'
        return repr_string


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

    def cell_at(self, i, j):
        return self._components[i * self._col + j]

    def draw(self, **kwargs):
        super().draw(**kwargs)
        self.draw_grid_line()

    def draw_grid_line(self):
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


