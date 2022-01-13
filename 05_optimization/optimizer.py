class Optimizer(object):
    def __init__(self, city, scene):
        """ An optimizer that iteratively optimizes a given city grid.
        
        Args:
            city (City): The city to be optimized.
            scene (Scene): The scene in which the city is rendered, used to compute a sunlight score.
        """
        self._city = city
        self._scene = scene

    @property
    def scene(self):
        return self._scene

    @property
    def city(self):
        return self._city

    def step(self, verbose=False):
        """ Performs one optimization step.
        Implement your optimization code here.

        Args:
            verbose (bool): If set to True, prints the city grid to the console each step. 
        """
        # TODO: Implement a step that smartly improves the city grid.
        current_score = self.score()
        self.city.swap(0, 0, 1, 1)
        new_score = self.score()
        # if new_score < current_score:
        #     self.city.swap(0, 0, 1, 1)
        #     return current_score
        if verbose: 
            print(self.city)
        return new_score

    def optimize(self, n_steps=100):
        """ Runs the optimizer for a fixed number of steps.
        Change this method to add a stopping criterion,
        e.g., if your score is not changing for a number of iterations,
        stop and return the current score.

        Args:
            n_steps (int): the number of steps to iterate.
        """
        self.city.reset()
        print('Optimizing city...')
        for i in range(n_steps):
            print('Step {}'.format(i), end='\r')
            score = self.step()
            # TODO: Add a stopping criterion, so you don't run unnecessary steps.
        print('\nDone! Final score: {}'.format(score))

    def score(self):
        """ Computes the score for your city.
        Complete this function by adding extra rules that enforce a good city planning.
        We've given you a start: here we compute the sunlight that hits each building.
        """
        total_score = 0
        # TODO: Implement a score based on rules you define.
        return total_score