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
    target_fitness = {
        0: {"pareto_front": 0, "crowding_distance": float("inf")},
        1: {"pareto_front": 0, "crowding_distance": 1.2},
        2: {"pareto_front": 0, "crowding_distance": 1.1},
        3: {"pareto_front": 0, "crowding_distance": 0.8},
        4: {"pareto_front": 0, "crowding_distance": float("inf")},
        5: {"pareto_front": 1, "crowding_distance": float("inf")},
        6: {"pareto_front": 1, "crowding_distance": 1.2},
        7: {"pareto_front": 1, "crowding_distance": 1.1},
        8: {"pareto_front": 1, "crowding_distance": float("inf")}
    }
    for individual_id, individual in population.items():
        fitness = individual.fitness
        assert isinstance(fitness, dict)
        assert "pareto_front" in fitness.keys()
        assert "crowding_distance" in fitness.keys()
        assert fitness == target_fitness[individual_id]


def test_evaluate_max_obs():
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
    non_dominated_sorter_kwargs = {"greater_is_better_dict": {0: True, 1: True}, "max_n_obs": 4}
    crowding_distance_sorter_kwargs = {"greater_is_better_dict": {0: True, 1: True}}
    evaluator = Evaluator(non_dominated_sorter_kwargs, crowding_distance_sorter_kwargs)
    evaluator.evaluate(population)
    target_fitness = {
        0: {"pareto_front": 0, "crowding_distance": float("inf")},
        1: {"pareto_front": 0, "crowding_distance": 1.2},
        2: {"pareto_front": 0, "crowding_distance": 1.1},
        3: {"pareto_front": 0, "crowding_distance": 0.8},
        4: {"pareto_front": 0, "crowding_distance": float("inf")},
        5: {},
        6: {},
        7: {},
        8: {}
    }
    for individual_id, individual in population.items():
        fitness = individual.fitness
        assert isinstance(fitness, dict)
        assert fitness == target_fitness[individual_id]
