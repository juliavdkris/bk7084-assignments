from bk7084.math import Vec3, Mat4
from bk7084.scene import Building

from components import *

class Skyscraper(Building):
    def __init__(self, name=None):
        super().__init__(name=name)
        wall = Wall(1.0, 1.0, texture1='textures/checker_small.png', texture2='textures/checker_color.png')
        wall2 = Wall(1.0, 1.0, texture1='textures/checker_huge.png', texture2='textures/checker_large.png')
        wall2.transform = Mat4.from_translation(Vec3(1.0, 0.0, 0.0))
        wall3 = Wall(1.0, 1.0, texture1='textures/checker_small.png', texture2='textures/checker_color.png')
        wall3.transform = Mat4.from_rotation_y(90, True) * Mat4.from_translation(Vec3(1.4, 0.0, 0.0))

        self.append(wall)
        self.append(wall2, wall)
        self.append(wall3, wall)