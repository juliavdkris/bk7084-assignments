from bk7084.math import Vec3, Mat4
from bk7084.scene import Building

from components import *

class Skyscraper(Building):
    def __init__(self, num_floors, max_width):
        super().__init__(name='skyscraper')
        wall1 = Wall(2, 2)
        wall1.transform = Mat4.from_translation(Vec3(0, 0, 1))
        wall2 = SimpleWall(2, 2)
        wall2.transform = Mat4.from_translation(Vec3(1, 0, 0)) * Mat4.from_rotation_y(90, True)
        wall3 = Wall(2, 2)
        wall3.transform = Mat4.from_translation(Vec3(0, 0, -1)) * Mat4.from_rotation_y(180, True)
        wall4 = SimpleWall(2, 2)
        wall4.transform = Mat4.from_translation(Vec3(-1, 0, 0)) * Mat4.from_rotation_y(-90, True)

        self.append(wall1)
        self.append(wall2)
        self.append(wall3)
        self.append(wall4)