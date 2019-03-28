"""
This module provides testing capabilities for the NonDominatedSorter class.
"""
import numpy as np

from fut_squad_evolver.nsga2.sorter.non_dominated_sorter import NonDominatedSorter, _is_better


def test_is_better():
    assert not _is_better(1, 2, True, 0)
    assert _is_better(1, 2, False, 0)
    assert not _is_better(2, 1, True, 1)
    assert not _is_better(1, 2, False, 1)
    assert _is_better(3, 1, True, 1)
    assert _is_better(1, 3, False, 1)


def test_sort():
    population = {
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
    sorter = NonDominatedSorter({0: True, 1: True})
    pareto_fronts = sorter.sort(population)
    target_fronts = [[0, 1, 2, 3, 4], [5, 6, 7, 8]]
    assert pareto_fronts == target_fronts
