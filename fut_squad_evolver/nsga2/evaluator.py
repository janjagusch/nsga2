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
        phenotypes = {individual_id: individual.phenotype for individual_id, individual in population.items()}
        pareto_front_ids = self.non_dominated_sorter.sort(phenotypes)
        pareto_fronts = [{individual_id: phenotypes[individual_id] for individual_id in front} for front in pareto_front_ids]
        crowding_distance_fronts = self.crowding_distance_sorter.sort(pareto_fronts)
        for front_level, front in enumerate(crowding_distance_fronts):
            for individual_id, crowding_distance in front.items():
                individual = population[individual_id]
                individual.fitness = {}
                individual.fitness["pareto_front"] = front_level
                individual.fitness["crowding_distance"] = crowding_distance
        return population
