import numpy as np
import pandas as pd


class CrowdingDistanceSorter:

    def __init__(self, greater_is_better_dict):
        self.greater_is_better_dict = greater_is_better_dict

    def _calculate_crowding_distance(self, values, max_value, min_value):
        values = pd.Series(values).sort_values()
        previous_values = values.shift(1)
        next_values = values.shift(-1)
        neighbor_delta = np.abs(next_values - previous_values)
        min_max_delta = np.abs(max_value - min_value)
        crowding_distance = (neighbor_delta / min_max_delta).fillna(float("inf"))
        crowding_distance = crowding_distance.to_dict()
        return crowding_distance

    def _front_sort(self, front, min_max_dict):
        crowding_distance = {key: 0 for key in front.keys()}
        for dim_key, min_max in min_max_dict.items():
            max_value = min_max["max"]
            min_value = min_max["min"]
            values = {obs_key: obs_val[dim_key] for obs_key, obs_val in front.items()}
            temp_cd = self._calculate_crowding_distance(values, max_value, min_value)
            for cd_key, cd_val in temp_cd.items():
                crowding_distance[cd_key] += cd_val
        return crowding_distance

    def sort(self, pareto_fronts):
        min_max_dict = {}
        for key in self.greater_is_better_dict.keys():
            min_max_dict[key] = {}
            min_max_dict[key]["min"] = np.min([phenotype[key] for front in pareto_fronts for phenotype in front.values()])
            min_max_dict[key]["max"] = np.max([phenotype[key] for front in pareto_fronts for phenotype in front.values()])
        return [self._front_sort(front, min_max_dict) for front in pareto_fronts]
