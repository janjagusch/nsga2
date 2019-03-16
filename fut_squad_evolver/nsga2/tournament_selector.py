import numpy as np


class TournamentSelector:

    def __init__(self, population_size):
        self.population_size = population_size

    def _select(self, individual_a, individual_b):
        fitness_a = individual_a["fitness"]
        fitness_b = individual_b["fitness"]
        if fitness_a["rank"] < fitness_b["rank"]:
            return individual_a
        elif fitness_a["rank"] == fitness_b["rank"]:
            if fitness_a["crowding_distance"] > fitness_b["crowding_distance"]:
                return individual_a
            if fitness_a["crowding_distance"] == fitness_b["crowding_distance"]:
                return np.random.choice([individual_a, individual_b])
            return individual_b
        return individual_b

    def populate(self, population):
        new_population = []
        for i in range(self.population_size):
            individual_a = np.random.choice(population)
            individual_b = np.random.choice(population)
            new_population.append(self._select(individual_a, individual_b))
        return new_population
