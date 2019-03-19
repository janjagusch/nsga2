import numpy as np

from fut_squad_evolver.nsga2.sorter.crowding_distance_sorter import CrowdingDistanceSorter
from fut_squad_evolver.nsga2.individual import Individual


def test_front_sort():
    front = {
        0: {0: 0, 1: 10},
        1: {0: 1, 1: 8},
        2: {0: 2, 1: 3},
        3: {0: 3, 1: 2},
        4: {0: 4, 1: 0}
    }
    greater_is_better_dict = {
        0: True,
        1: True
    }
    min_max_dict = {
        0: {"min": 0, "max": 10},
        1: {"min": 0, "max": 10}
    }
    target_values = {
        0: float("inf"),
        1: 0.9,
        2: 0.8,
        3: 0.5,
        4: float("inf")
    }
    sorter = CrowdingDistanceSorter(greater_is_better_dict)
    result = sorter._front_sort(front, min_max_dict)
    for key, value in result.items():
        assert np.isclose(value, target_values[key])


def test_sort():
    phenotypes = [
        {
            0: {0: 0, 1: 10},
            1: {0: 1, 1: 8},
            2: {0: 2, 1: 3},
            3: {0: 3, 1: 2},
            4: {0: 4, 1: 0}
        },
        {
            5: {0: 0, 1: 9},
            6: {0: 1, 1: 7},
            7: {0: 2, 1: 2},
            8: {0: 3, 1: 1}
        }
    ]
    pareto_fronts = []
    for phenotype_front in phenotypes:
        front = {}
        for key, value in phenotype_front.items():
            indiviual = Individual(None, indiviual_id=key)
            indiviual.phenotype = value
            front[indiviual.indiviual_id] = indiviual
        pareto_fronts.append(front)
    greater_is_better_dict = {
        0: True,
        1: True
    }
    target_values = [
        {
            0: float("inf"),
            1: 1.2,
            2: 1.1,
            3: 0.8,
            4: float("inf")
        },
        {
            5: float("inf"),
            6: 1.2,
            7: 1.1,
            8: float("inf")
        }
    ]
    sorter = CrowdingDistanceSorter(greater_is_better_dict)
    result = sorter.sort(pareto_fronts)
    for front, target_front in zip(result, target_values):
        for key, value in front.items():
            assert np.isclose(value, target_front[key])
