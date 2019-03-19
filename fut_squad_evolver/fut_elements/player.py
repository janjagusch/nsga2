"""
This class describes a player card.
"""

import pandas as pd


PANDAS_PLAYER_CONVERSION_MAP = {
    "player_id": "player_id",
    "overall": "overall",
    "club": "club",
    "league": "league",
    "nationality": "nationality",
    "position": "position",
    "metal": "metal",
    "is_rare": "is_rare",
    "price": "price",
    "base_id": "base_id"
}


PLAYER_PANDAS_CONVERSION_MAP =\
    {value: key for key, value in PANDAS_PLAYER_CONVERSION_MAP.items()}


class Player:

    def __init__(self, player_id, overall, club, league, nationality, position,
                 metal, is_rare, price, base_id, base=None):
        self.player_id = player_id
        self.overall = overall
        self.club = club
        self.league = league
        self.nationality = nationality
        self.position = position
        self.metal = metal
        self.is_rare = is_rare
        self.price = price
        self.base_id = base_id
        self.base = base

    def __repr__(self):
        repr = "{}(player_id={}, overall={}, club={}, league={}, \
        nationality={}, position={}, price={}, base_id={})"\
        .format(self.__class__.__name__, self.player_id, self.overall, self.club, self.league,
                self.nationality, self.position, self.price, self.base_id)
        return repr

    @staticmethod
    def _from_pandas(pandas_player):
        return Player(**pandas_player[PANDAS_PLAYER_CONVERSION_MAP.keys()]
                      .rename(PANDAS_PLAYER_CONVERSION_MAP).to_dict())

    def _to_pandas(self):
        return pd.Series(self.__dict__)[PLAYER_PANDAS_CONVERSION_MAP.keys()]\
            .rename(PLAYER_PANDAS_CONVERSION_MAP)
