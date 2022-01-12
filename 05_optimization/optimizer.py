
class Optimizer(object):
    def __init__(self, scene, city):
        self._scene = scene
        self._city = city

    def iteration(self):
        """
        Implement your optimization code here.
        This function is called everytime the scene is drawn.
        """
        current_score = self.score()
        self._city.swap(0, 0, 1, 1)
        if self.score() < current_score:
            self._city.swap(0, 0, 1, 1)
        return

    def score(self):
        total_score = 0
        buildings = self._city.buildings
        for i in range(1, len(buildings)):
            total_score += self._scene.energy_of_building(buildings[i], save_energy_map=False)
        return total_score