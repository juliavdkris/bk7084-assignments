from bk7084.math import *
from components import *


class Skyscraper:
    """A basic skyscraper class that procedurally generates
    a skyscraper given a number of floors and width.

    Args:
        num_floors (int):
            Number of floors to generate.
        max_width (float):
            The maximum width for each component.
    """
    def __init__(self, app, num_floors, max_width):
        self.num_floors = num_floors
        # Spawn the building and save the id
        self.building = app.spawn_building()
        self.building.set_visible(True)
        for i in range(self.num_floors):
            # To place each floor higher than the previous one,
            # we parent all components to one 'base' component (floor1, see below).
            # Then we only have to move the base component up higher
            # and the framework takes care of the rest.
            floor1 = app.add_mesh(create_basic_floor(max_width, max_width), parent=self.building)
            # Place the base component higher each time (i)
            floor1.set_transform(Mat4.from_translation(Vec3(0, max_width * i, 0)))
            floor1.set_visible(True)
            floor2 = app.add_mesh(create_basic_floor(max_width, max_width), parent=floor1)
            floor2.set_transform(Mat4.from_translation(Vec3(0, max_width, 0)))
            floor2.set_visible(True)
            wall1 = app.add_mesh(BasicWindowWallMesh(max_width, max_width), parent=floor1)
            wall1.set_transform(Mat4.from_translation(Vec3(0, max_width / 2, max_width / 2)))
            wall1.set_visible(True)
            wall2 = app.add_mesh(BasicWallMesh(max_width, max_width), parent=floor1)
            wall2.set_transform(Mat4.from_translation(Vec3(max_width / 2, max_width / 2, 0)) * Mat4.from_rotation_y(90, True))
            wall2.set_visible(True)
            wall3 = app.add_mesh(BasicWallMesh(max_width, max_width), parent=floor1)
            wall3.set_transform(Mat4.from_translation(Vec3(0, max_width / 2, -max_width / 2)) * Mat4.from_rotation_y(180, True))
            wall3.set_visible(True)
            wall4 = app.add_mesh(BasicWallMesh(max_width, max_width), parent=floor1)
            wall4.set_transform(Mat4.from_translation(Vec3(-max_width / 2, max_width / 2, 0)) * Mat4.from_rotation_y(-90, True))
            wall4.set_visible(True)


class Highrise:
    """A highrise class that procedurally generates
    a highrise building given a number of floors and width.

    Args:
        num_floors (int):
            Number of floors to generate.
        max_width (float):
            The maximum width for each component.
    """
    def __init__(self, num_floors, max_width):
        super().__init__(name='highrise')


class Office:
    """An office class that procedurally generates
    a office building given a number of floors and width.

    Args:
        num_floors (int):
            Number of floors to generate.
        max_width (float):
            The maximum width for each component.
    """
    def __init__(self, num_floors, max_width):
        super().__init__(name='office')