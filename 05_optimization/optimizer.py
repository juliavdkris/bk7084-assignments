from bk7084.graphics import PointLight
from bk7084.math import Mat4, Vec4, Vec3


class Optimizer(object):
    def __init__(self, scene, city):
        self._scene = scene
        self._city = city

    def optimize(self):
        print('Optimizing...')
        for i in range(100):
            print('Iteration {}'.format(i), end='\r')
            self.iteration()
        score = self.score()
        print('\nOptimization complete!')
        print('Score: {}'.format(score))

    def iteration(self):
        """
        Implement your optimization code here.
        """
        current_score = self.score()
        self._city.swap(0, 0, 1, 1)
        if self.score() < current_score:
            self._city.swap(0, 0, 1, 1)
        return

    def compute_light_of_plot(self, i, j, light):
        """
        Compute the light energy of a plot.
        Args:
            i (int):
                The row number of the plot in range [0, 8).
            j (int):
                The col number of the plot in range [0, 8).
            light (Light):
                The light that you want to compute with.
        Returns:
            Energy ratio in range [0.0, 1.0]
        """
        cell = self._city.grid.cell_at(i, j)
        energy = self._scene.energy_of_building_component(self._city.grid, cell, light)
        return energy

    def compute_light_of_building(self, i, j, light):
        building, transform = self._city.building_at(i, j)
        energy = self._scene.energy_of_building(building, light, mesh_transform=transform)
        return energy

    def score(self):
        """
        Implement your city score here.
        We've given you a start: here we compute the sunlight that hits each building.
        """
        total_score = 0
        return total_score