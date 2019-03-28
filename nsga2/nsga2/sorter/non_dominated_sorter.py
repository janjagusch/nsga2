"""
This module implements the non-dominated sorting algorithm.
"""
import numpy as np


def _is_better(val1, val2, greater_is_better, threshold):
    """
    Checks whether val1 is better than val2.
    """
    if greater_is_better:
        return val1 > val2 + threshold
    return val1 < val2 - threshold


def _make_domination_array(dim, greater_is_better, threshold):
    """
    Calculates a domination array dim x dim.
    """
    xx_vals, yy_vals = np.meshgrid(dim, dim)
    return _is_better(xx_vals, yy_vals, greater_is_better, threshold)


def _make_not_dominated(domination_arrays):
    """
    Calculates non-dominated array from list of domination arrays.
    """
    better_in_any = np.any(domination_arrays, axis=0)
    not_worse_in_any = np.invert(better_in_any.T)
    dominates = np.logical_and(better_in_any, not_worse_in_any)
    not_dominated = np.invert(dominates.T)
    return not_dominated


class NonDominatedSorter:
    """
    This class represents the non-dominated sorting algorithm.
    """
    def __init__(self, greater_is_better_dict, threshold_dict=None, max_n_obs=None, _temp_id_name="_id"):
        self.greater_is_better_dict = greater_is_better_dict
        if threshold_dict is None:
            threshold_dict = {}
        for k in greater_is_better_dict.keys():
            if k not in threshold_dict.keys():
                threshold_dict[k] = 0
        self.threshold_dict = threshold_dict
        self.max_n_obs = max_n_obs
        self._temp_id_name = _temp_id_name

    def _make_domination_arrays(self, dataset):
        domination_arrays = []
        for key, greater_is_better in self.greater_is_better_dict.items():
            threshold = self.threshold_dict[key]
            objective = [obs[key] for obs in dataset]
            domination_arrays.append(
                _make_domination_array(objective, greater_is_better, threshold))
        domination_arrays = np.array(domination_arrays)
        return domination_arrays

    def _get_pareto_fronts(self, dataset, not_dominated):
        n_obs = 0
        pareto_fronts = []
        if not isinstance(dataset, np.ndarray):
            dataset = np.array(dataset)
        while dataset.size > 0:
            champions = np.argwhere(np.all(not_dominated, axis=0)).reshape(-1,)
            # print(champions)
            # print(dataset)
            pareto_fronts.append(dataset[champions])
            not_dominated = np.delete(not_dominated, champions, axis=0)
            not_dominated = np.delete(not_dominated, champions, axis=1)
            dataset = np.delete(dataset, champions, axis=0)
            n_obs += champions.size
            if self.max_n_obs is not None and n_obs >= self.max_n_obs:
                break
        return pareto_fronts

    def sort(self, dataset):
        """
        Sorts the input dataset.
        """
        # add key to values of dict
        new_dataset = {}
        for key, value in dataset.items():
            new_value = value
            new_value[self._temp_id_name] = key
            new_dataset[key] = new_value
        # print(new_dataset)
        dataset_values = list(new_dataset.values())
        domination_arrays = self._make_domination_arrays(dataset_values)
        not_dominated = _make_not_dominated(domination_arrays)
        pareto_fronts = self._get_pareto_fronts(dataset_values, not_dominated)
        new_pareto_front = [[value[self._temp_id_name] for value in front] for front in pareto_fronts]
        return new_pareto_front
