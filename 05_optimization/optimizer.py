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

    def score(self):
        """
        Implement your city score here.
        We've given you a start: here we compute the sunlight that hits each building.
        """
        total_score = 0
        return total_score