import numpy as np


class TournamentSelector:

    def __init__(self, population_size):
        self.population_size = population_size

    def _select(self, fitness_tuple_a, fitness_tuple_b):
        individual_id_a, fitness_a = fitness_tuple_a
        individual_id_b, fitness_b = fitness_tuple_b
        if fitness_a["pareto_front"] < fitness_b["pareto_front"]:
            return individual_id_a
        elif fitness_a["pareto_front"] == fitness_b["pareto_front"]:
            if fitness_a["crowding_distance"] > fitness_b["crowding_distance"]:
                return individual_id_a
            if fitness_a["crowding_distance"] == fitness_b["crowding_distance"]:
                return np.random.choice([individual_id_a, individual_id_b])
            return individual_id_b
        return individual_id_b

    def populate(self, population):
        tournament_pool = [individual for individual in population.values() if individual.fitness != {}]
        champions = []
        for i in range(self.population_size):
            individual_id_a = np.random.choice(list(population.keys()))
            individual_id_b = np.random.choice(list(population.keys()))
            individual_a = population[individual_id_a]
            individual_b = population[individual_id_b]
            champion_id = self._select((individual_id_a, individual_a.fitness), (individual_id_b, individual_b.fitness))
            champions.append(population[champion_id])
        return champions
