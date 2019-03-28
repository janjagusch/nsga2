from fut_squad_evolver.nsga2.selector import TournamentSelector
from fut_squad_evolver.nsga2.individual import Individual


def test_select():
    selector = TournamentSelector(10)
    # lower pareto_front
    fitness_tuple_a = 1, {"pareto_front": 0, "crowding_distance": 1}
    fitness_tuple_b = 2, {"pareto_front": 1, "crowding_distance": 1}
    champion_id = selector._select(fitness_tuple_a, fitness_tuple_b)
    assert champion_id == 1
    # higher pareto_front
    fitness_tuple_a = 1, {"pareto_front": 1, "crowding_distance": 1}
    fitness_tuple_b = 2, {"pareto_front": 0, "crowding_distance": 1}
    champion_id = selector._select(fitness_tuple_a, fitness_tuple_b)
    assert champion_id == 2
    # same pareto front, higher crowding_distance
    fitness_tuple_a = 1, {"pareto_front": 0, "crowding_distance": 2}
    fitness_tuple_b = 2, {"pareto_front": 0, "crowding_distance": 1}
    champion_id = selector._select(fitness_tuple_a, fitness_tuple_b)
    assert champion_id == 1
    # same pareto front, lower crowding_distance
    fitness_tuple_a = 1, {"pareto_front": 0, "crowding_distance": 1}
    fitness_tuple_b = 2, {"pareto_front": 0, "crowding_distance": 2}
    champion_id = selector._select(fitness_tuple_a, fitness_tuple_b)
    assert champion_id == 2
    # same pareto front, same crowding_distance
    fitness_tuple_a = 1, {"pareto_front": 0, "crowding_distance": 1}
    fitness_tuple_b = 2, {"pareto_front": 0, "crowding_distance": 1}
    champion_id = selector._select(fitness_tuple_a, fitness_tuple_b)
    assert champion_id in (1, 2)


def test_populate():
    selector = TournamentSelector(5)
    fitness_map = {
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
    population = {}
    for individual_id, fitness in fitness_map.items():
        individual = Individual(None, individual_id=individual_id)
        individual.fitness = fitness
        population[individual_id] = individual
    champions = selector.populate(population)
    assert len(champions) == 5
    for individual in champions:
        assert isinstance(individual, Individual)
