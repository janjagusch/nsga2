"""
This class represents the Crossover operator for the genetic algorithm.
"""
from copy import deepcopy

import numpy as np

from fut_squad_evolver.nsga2.individual import Individual


class Crossover:

    def __init__(self, crossover_probability):
        self.crossover_probability = crossover_probability

    def _copy_genotype(self, genotype_a, genotype_b):
        return deepcopy(genotype_a), deepcopy(genotype_b)

    def _crossover_genotype(self, genotype_a, genotype_b):
        """
        Takes the parent's genotype and prouces two new genotypes.
        """
        return {}, {}

    def _crossover_parents(self, genotype_a, genotype_b):
        if np.random.uniform() < self.crossover_probability:
            return self._crossover_genotype(genotype_a, genotype_b)
        return self._copy_genotype(genotype_a, genotype_b)

    def crossover(self, individual_a, individual_b):
        """
        Takes the genotype of the parents and creates two new individuals.
        """
        parent_genotype_a = individual_a.genotype
        parent_genotype_b = individual_b.genotype
        child_genotype_a, child_genotype_b = self._crossover_parents(parent_genotype_a, parent_genotype_b)
        child_a = Individual(child_genotype_a)
        child_b = Individual(child_genotype_b)
        return child_a, child_b
