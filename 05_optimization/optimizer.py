from city import BuildingType, City

import numpy as np

from random import randint
from collections import deque


class Plot:
	def __init__(self, row, col):
		self.row = row
		self.col = col

	def __eq__(self, other):
		return self.row == other.row and self.col == other.col

	def __hash__(self):
		return hash((self.row, self.col))


# Commutative pair of plots
class Swap:
	def __init__(self, p1: Plot, p2: Plot):
		self._pair = frozenset([p1, p2])

	def __eq__(self, other):
		return self._pair == other._pair

	def __hash__(self):
		return hash(self._pair)

	def unpack(self) -> tuple[int, int, int, int]:
		p1, p2 = self._pair
		return p1.row, p1.col, p2.row, p2.col


class Cache:
	def __init__(self, city):
		self._city = city
		self._cache: dict[int, tuple[list[BuildingType], float]] = {}

	def get(self, plots) -> float:
		plots_hash = hash(tuple(plots))
		if plots_hash in self._cache:
			_, score = self._cache[plots_hash]
		else:
			score = sum(self._city.compute_sunlight_scores())
			self._cache[plots_hash] = (plots, score)
		return score


class Optimizer:
	SWAPS_PER_STEP = 10
	TABU_DEQUE_SIZE = 100

	def __init__(self, city):
		"""An optimizer that iteratively optimizes a given city grid."""
		self._city = city
		self._scores = self._city.compute_sunlight_scores()
		self._best = self._city._plots.copy()
		self._best_value = sum(self._scores)
		self._cache = Cache(city)
		self._tabu: deque[Swap] = deque(maxlen=self.TABU_DEQUE_SIZE)


	def score(self) -> float:
		'''Returns the score of the current city layout.
		Criteria:
			- (w=0.3) Skyscrapers and highrises should be close to the center of the city
			- (w=0.4) Houses should be close to parks
			- (w=0.2) Offices should be close to both a house and a highrise or skyscraper
			- (w=0.1) Parks can only have one other parks directly adjacent
		'''
		w = [0.3, 0.4, 0.2, 0.1]
		s1 = s2 = s3 = s4 = 0

		c1 = self._city.count_buildings(BuildingType.SKYSCRAPER) + self._city.count_buildings(BuildingType.HIGHRISE)
		c2 = self._city.count_buildings(BuildingType.HOUSE)
		c3 = self._city.count_buildings(BuildingType.OFFICE)
		c4 = self._city.count_buildings(BuildingType.PARK)

		for row in range(self._city.rows):
			for col in range(self._city.cols):
				building_type = self._city.get_building_type(row, col)

				# Skyscrapers and highrises should be close to the center of the city
				if building_type == BuildingType.SKYSCRAPER or building_type == BuildingType.HIGHRISE:
					manhattan_dist_from_center = abs(row - self._city.rows // 2) + abs(col - self._city.cols // 2)
					s1 += 1 / manhattan_dist_from_center

				# Houses should be close to parks
				elif building_type == BuildingType.HOUSE:
					s2 += 1 / self._city.dist_to_nearest(row, col, BuildingType.PARK)

				# Offices should be close to both a house and a highrise or skyscraper
				elif building_type == BuildingType.OFFICE:
					dist_to_house = self._city.dist_to_nearest(row, col, BuildingType.HOUSE)
					dist_to_highrise = self._city.dist_to_nearest(row, col, BuildingType.HIGHRISE)
					dist_to_skyscraper = self._city.dist_to_nearest(row, col, BuildingType.SKYSCRAPER)
					s3 += 1 / max(dist_to_house, min(dist_to_highrise, dist_to_skyscraper))

				# Parks can only have one other parks directly adjacent
				elif building_type == BuildingType.PARK:
					s4 += 1 if self._city.count_adjacent(row, col, BuildingType.PARK) <= 1 else 0

		s1 /= c1
		s2 /= c2
		s3 /= c3
		s4 /= c4

		return w[0] * s1 + w[1] * s2 + w[2] * s3 + w[3] * s4


	def random_plot(self) -> Plot:
		'''Returns a random plot in the city.'''
		return Plot(randint(0, self._city._plots_per_row - 1), randint(0, self._city._plots_per_col - 1))


	def random_swap(self) -> Swap:
		'''Returns a random swap of two plots in the city.'''
		return Swap(self.random_plot(), self.random_plot())


	def score_swap(self, swap: Swap) -> float:
		'''Returns the score of a swap without modifying the city. Uses cache if available.'''
		self._city.swap_buildings(*swap.unpack())

		plots = self._city._plots
		score = self._cache.get(plots)

		self._city.swap_buildings(*swap.unpack())

		return score


	def step(self, print_info=False):
		"""Performs a single optimization step.
		Args:
			print_info (bool):
				Whether to print information about the optimization step.
		"""

		potential_swaps = [swap for _ in range(self.SWAPS_PER_STEP) if (swap := self.random_swap()) not in self._tabu]  # What if too many swaps are taboo?

		scores = [self.score_swap(swap) for swap in potential_swaps]
		best_swap = potential_swaps[np.argmax(scores)]

		# Update current
		self._city.swap_buildings(*best_swap.unpack())
		self._tabu.append(best_swap)

		# If better than best, update best
		if max(scores) > sum(self._scores):
			self._best = self._city._plots.copy()
			self._best_value = sum(self._scores)

		#  Hint: You can use the function `compute_sunlight_scores` of the City class
		#  to compute the sunlight scores
		new_scores = self._city.compute_sunlight_scores()
		if print_info:
			print("New scores: ", new_scores)
			print("New scores sum: ", sum(new_scores))
			print("New city layout: ")
			self._city.print_plots()
		return sum(new_scores)


	def optimize(self, n_steps=100, print_info=False):
		"""
		Runs the optimizer for a fixed number of steps.
		Args:
			n_steps (int):
				The number of optimization steps.
			print_info (bool):
				Whether to print information about the optimization step.
		"""
		# TODO: Change this method to add a stopping criterion, e.g. stop when
		#  the score does not improve anymore.
		self._city.reset_grid()
		print("Initial scores: ", self._city.compute_sunlight_scores())
		print("Initial scores sum: ", sum(self._city.compute_sunlight_scores()))
		print("Initial city layout: ")
		self._city.print_plots()
		print("Optimizing...")
		for i in range(n_steps):
			print(f"Step: {i}", end="\r")
			score = self.step(print_info)
			# TODO: Add a stopping criterion here.
		print(f"\nDone! Final score: {score}")