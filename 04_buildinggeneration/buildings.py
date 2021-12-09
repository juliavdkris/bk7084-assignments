from bk7084.math import Vec3, Mat4
from bk7084.scene import Building

from components import *

class Skyscraper(Building):
    """A basic skyscraper class that procedurally generates
    a skyscraper given a number of floors and width.

    Args:
        num_floors (int):
            Number of floors to generate.
        max_width (float):
            The maximum width for each component.
    """
    def __init__(self, num_floors, max_width):
        super().__init__(name='skyscraper')
        num_floors = min(10, num_floors)
        for i in range(num_floors):
            # To place each floor higher than the previous one,
            # we parent all components to one 'base' component (floor1, see below).
            # Then we only have to move the base component up higher
            # and the framework takes care of the rest.
            floor1 = BasicFloor(max_width, max_width)
                                                    # Place the base component higher each time (i)
            floor1.transform = Mat4.from_translation(Vec3(0, max_width * i, 0))
            floor2 = BasicFloor(max_width, max_width)
            floor2.transform = Mat4.from_translation(Vec3(0, max_width, 0))
            wall1 = WindowWall(max_width, max_width)
            wall1.transform = Mat4.from_translation(Vec3(0, 0, max_width / 2))
            wall2 = BasicWall(max_width, max_width)
            wall2.transform = Mat4.from_translation(Vec3(max_width / 2, 0, 0)) * Mat4.from_rotation_y(90, True)
            wall3 = WindowWall(max_width, max_width)
            wall3.transform = Mat4.from_translation(Vec3(0, 0, -max_width / 2)) * Mat4.from_rotation_y(180, True)
            wall4 = BasicWall(max_width, max_width)
            wall4.transform = Mat4.from_translation(Vec3(-max_width / 2, 0, 0)) * Mat4.from_rotation_y(-90, True)

            # This is where we add all the components and parent them to floor1
            self.append(floor1)
            self.append(floor2, parent=floor1)
            self.append(wall1, parent=floor1)
            self.append(wall2, parent=floor1)
            self.append(wall3, parent=floor1)
            self.append(wall4, parent=floor1)


class Highrise(Building):
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


class Office(Building):
    """An office class that procedurally generates
    a office building given a number of floors and width.

    Args:
        num_floors (int):
            Number of floors to generate.
        max_width (float):
            The maximum width for each component.
    """
    def __init__(self, num_floors, max_width):
        super().__init__(name='highrise')