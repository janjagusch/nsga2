"""
This module describes the Base class, which is a player that can contain
multiple player cards.
"""


import pandas as pd


PANDAS_BASE_CONVERSION_MAP = {
    "base_id": "base_id",
    "player_name": "name",
    "player_extended_name": "extended_name",
    "age": "age",
    "date_of_birth": "date_of_birth",
    "height": "height",
    "weight": "weight",
    "intl_rep": "international_reputation"
}


BASE_PANDAS_CONVERSION_MAP =\
    {value: key for key, value in PANDAS_BASE_CONVERSION_MAP.items()}


class Base:

    def __init__(self, base_id, name, extended_name, age,
                 date_of_birth, height, weight, international_reputation,
                 players=None):
        self.base_id = base_id
        self.name = name
        self.extended_name = extended_name
        self.age = age
        self.date_of_birth = date_of_birth
        self.height = height
        self.weight = weight
        self.international_reputation = international_reputation
        if players is None:
            players = {}
        self.players = players

    def __repr__(self):
        repr = "{}(base_id={}, name={}, age={}, height={}, weight={}, \
        international_reputation={})"\
        .format(self.__class__.__name__, self.base_id, self.name, self.age,
                self.height, self.weight, self.international_reputation)
        return repr

    @staticmethod
    def _from_pandas(pandas_base):
        return Base(**pandas_base[PANDAS_BASE_CONVERSION_MAP.keys()]
                    .rename(PANDAS_BASE_CONVERSION_MAP).to_dict())

    def _to_pandas(self):
        return pd.Series(self.__dict__)[BASE_PANDAS_CONVERSION_MAP.keys()]\
            .rename(BASE_PANDAS_CONVERSION_MAP)
