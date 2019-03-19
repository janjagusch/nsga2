from fut_squad_evolver.nsga2.evaluator import Evaluator
from fut_squad_evolver.nsga2.individual import Individual


def test_evaluate():
    phenotypes = {
        0: {0: 0, 1: 10},
        1: {0: 1, 1: 8},
        2: {0: 2, 1: 3},
        3: {0: 3, 1: 2},
        4: {0: 4, 1: 0},
        5: {0: 0, 1: 9},
        6: {0: 1, 1: 7},
        7: {0: 2, 1: 2},
        8: {0: 3, 1: 1}
    }
    population = {}
    for key, value in phenotypes.items():
        individual = Individual(None, individual_id=key)
        individual.phenotype = value
        population[individual.individual_id] = individual
    non_dominated_sorter_kwargs = {"greater_is_better_dict": {0: True, 1: True}}
    crowding_distance_sorter_kwargs = {"greater_is_better_dict": {0: True, 1: True}}
    evaluator = Evaluator(non_dominated_sorter_kwargs, crowding_distance_sorter_kwargs)
    evaluator.evaluate(population)
    for individual in population:
        assert isinstance(individual.fitness, dict)
