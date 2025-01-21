import numpy as np

from random import randint
from copy import deepcopy


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


class Optimizer:
	SWAPS_PER_STEP = 10

	def __init__(self, city):
		"""An optimizer that iteratively optimizes a given city grid."""
		self._city = city
		self._scores = self._city.compute_sunlight_scores()
		self._best = city
		self._best_value = sum(self._scores)
		self._tabu: set[Swap] = set()


	def random_plot(self) -> Plot:
		return Plot(randint(0, self._city._plots_per_row - 1), randint(0, self._city._plots_per_col - 1))


	def random_swap(self) -> Swap:
		return Swap(self.random_plot(), self.random_plot())


	def score_swap(self, swap: Swap) -> float:
		copy = deepcopy(self._city)
		copy.swap_buildings(*swap.unpack())

		return sum(copy.compute_sunlight_scores())


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
		self._tabu.add(best_swap)

		# If better than best, update best
		if max(scores) > sum(self._scores):
			self._best = deepcopy(self._city)
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