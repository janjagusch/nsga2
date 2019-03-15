import numpy as np
import pandas as pd


class CrowdingDistanceSorter:

    def __init__(self, min_max_dict):
        self.min_max_dict = min_max_dict


    def _calculate_crowding_distance(self, values, max_value, min_value):
        values = pd.Series(values).sort_values()
        previous_values = values.shift(1)
        next_values = values.shift(-1)
        neighbor_delta = np.abs(next_values - previous_values)
        min_max_delta = np.abs(max_value - min_value)
        crowding_distance = (neighbor_delta / min_max_delta).fillna(float("inf"))
        crowding_distance = crowding_distance.to_dict()
        return crowding_distance


    def sort(self, front):
        crowding_distance = {key: 0 for key in front.keys()}
        for dim_key, min_max in self.min_max_dict.items():
            max_value = min_max["max"]
            min_value = min_max["min"]
            values = {obs_key: obs_val["objectives"][dim_key] for obs_key, obs_val in front.items()}
            temp_cd = self._calculate_crowding_distance(values, max_value, min_value)
            for cd_key, cd_val in temp_cd.items():
                crowding_distance[cd_key] += cd_val
        return crowding_distance
