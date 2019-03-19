from fut_squad_evolver.nsga2.sorter.non_dominated_sorter import NonDominatedSorter
from fut_squad_evolver.nsga2.sorter.crowding_distance_sorter import CrowdingDistanceSorter


class Evaluator:

    def __init__(self, non_dominated_sorter_kwargs, crowding_distance_sorter_kwargs):
        self.non_dominated_sorter = NonDominatedSorter(**non_dominated_sorter_kwargs)
        self.crowding_distance_sorter = CrowdingDistanceSorter(**crowding_distance_sorter_kwargs)

    def evaluate(self, population):
        """
        Fills the fitness attribute of each element in the population (inplace).
        """
        pareto_fronts = self.non_dominated_sorter.sort(population)
        crowding_distance_fronts = self.crowding_distance_sorter.sort(pareto_fronts)
        for front_level, front in enumerate(pareto_fronts):
            for indiviual_id, individual in front.items():
                indiviual.fitness = {}
                indiviual.fitness["pareto_front"] = front_level
                individual.fitness["crowding_distance"] = crowding_distance_fronts[front_level][indiviual_id]
        return population
