import numpy as np


class TournamentSelector:

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

    def select(self, population):
        tournament_pool = {key: individual for key, individual in population.items() if individual.fitness != {}}
        champions = []
        for i in range(len(population)):
            individual_id_a = np.random.choice(list(tournament_pool.keys()))
            individual_id_b = np.random.choice(list(tournament_pool.keys()))
            individual_a = tournament_pool[individual_id_a]
            individual_b = tournament_pool[individual_id_b]
            champion_id = self._select((individual_id_a, individual_a.fitness), (individual_id_b, individual_b.fitness))
            champions.append(tournament_pool[champion_id])
        return champions
