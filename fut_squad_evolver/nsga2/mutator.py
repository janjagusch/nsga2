"""
This class describes the Mutator operator for the genetic algorithm.
"""
import numpy as np


class Mutator:

    def __init__(self, mutation_probability):
        self.mutation_probability = mutation_probability

    def _mutate_genotype(self, genotype):
        pass

    def mutate(self, indiviual):
        if np.random.uniform() > self.mutation_probability:
            self._mutate_genotype(indiviual)
