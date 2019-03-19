import pandas as pd

from ..player import Player, PANDAS_PLAYER_CONVERSION_MAP, \
    PLAYER_PANDAS_CONVERSION_MAP
from ...utils.data_loader import PLAYERS


pandas_player = PLAYERS[PLAYERS["player_id"] == 6419].iloc[0]


def test_from_to_pandas():
    player = Player._from_pandas(pandas_player)
    assert isinstance(player, Player)
    for player_key, pandas_key in PLAYER_PANDAS_CONVERSION_MAP.items():
        assert player.__dict__[player_key] == pandas_player[pandas_key]
    pandas_player_2 = player._to_pandas()
    for key in PANDAS_PLAYER_CONVERSION_MAP.keys():
        assert pandas_player[key] == pandas_player_2[key]
