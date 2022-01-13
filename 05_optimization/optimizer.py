from bk7084.graphics import PointLight
from bk7084.math import Mat4, Vec4, Vec3


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
        self.city.swap(0, 0, 1, 1)
        new_score = self.score()
        if verbose:
            print(self.city)
            print('Score: {}'.format(new_score))
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
        We've given you a start: here we compute the sunlight that hits plot for a full day.
        """
        total_score = 0
        # If your program is too slow, comment out the next four lines
        # while you're testing other rules.
        # Don't forget to uncomment when you want to test all your rules.
        for i in range(self.city.row):
            for j in range(self.city.col):
                # You can also lower the number of hours to speed up computations
                total_score += self.compute_light_of_plot_day(i, j, hours=12)

        # TODO: Implement other rules to define your score
        return total_score

    def compute_light_of_plot_day(self, i, j, hours=12):
        """ Computes the light of a plot for a full day.
        This function can be very slow. You can reduce the time this function takes
        by shortening the number of hours that are computed.
        Args:
            i (int): The row number of the plot in range [0, 8).
            j (int): The col number of the plot in range [0, 8).
        """
        total_energy = 0
        for t in range(hours):
            self.scene._current_light = t
            total_energy += self.compute_light_of_plot(i, j, self.scene.current_light)
        self.scene._current_light = 0
        return total_energy  

    def compute_light_of_plot(self, i, j, light):
        """
        Compute the light energy of a plot.
        Args:
            i (int): The row number of the plot in range [0, 8).
            j (int): The col number of the plot in range [0, 8).
            light (Light): The light that you want to compute with.
        Returns:
            Energy ratio in range [0.0, 1.0]
        """
        cell = self.city.grid.cell_at(i, j)
        energy = self.scene.energy_of_building_component(self._city.grid, cell, light)
        return energy

    def compute_light_of_building(self, i, j, light):
        """
        Compute the light energy of a whole building.
            Args:
                i (int): The row number of the plot where the building is located.
                j (int): The col number of the plot where the building is located.
                light (Light): The light that you want to compute with.
            Returns:
                Energy ratio in range [0.0, 1.0]
            """
        building, transform = self.city.building_at(i, j)
        energy = self.scene.energy_of_building(building, light, mesh_transform=transform)
        return energy