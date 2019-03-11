import pandas as pd


def _calculate_crowding_distance(values, v_max, v_min, greater_is_better):
    ascending = True if greater_is_better else False
    values = pd.Series(values).sort_values(ascending=ascending)
    previous_values = values.shift(1)
    next_values = values.shift(-1)
    crowding_distance = ((next_values - previous_values) / (v_max - v_min)).\
        fillna(float("inf"))
    crowding_distance = crowding_distance.to_dict()
    return crowding_distance


def calculate_crowding_distance(front, min_max_dict, greater_is_better_dict):
    crowding_distance = {key: 0 for key in front.keys()}
    for dim_key, greater_is_better in greater_is_better_dict.items():
        v_max = min_max_dict[dim_key]["max"]
        v_min = min_max_dict[dim_key]["min"]
        values = {obs_key: obs_val["objectives"][dim_key] for obs_key, obs_val in front.items()}
        temp_cd = _calculate_crowding_distance(values, v_max, v_min, greater_is_better)
        for cd_key, cd_val in temp_cd.items():
            crowding_distance[cd_key] += cd_val
    return crowding_distance


front = {
    0: {"objectives": {0: 0, 1: 4}},
    1: {"objectives": {0: 1, 1: 3}},
    2: {"objectives": {0: 2, 1: 9}},
    3: {"objectives": {0: 3, 1: 1}},
    4: {"objectives": {0: 4, 1: 0}}
}

min_max_dict = {
    0: {"min": 0, "max": 4},
    1: {"min": 10, "max": 0}
}

greater_is_better_dict = {
    0: True,
    1: False
}


print(calculate_crowding_distance(front, min_max_dict, greater_is_better_dict))
