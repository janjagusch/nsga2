import pandas as pd

from ..base import Base, PANDAS_BASE_CONVERSION_MAP, BASE_PANDAS_CONVERSION_MAP
from ...utils.data_loader import PLAYERS


pandas_base = PLAYERS[PLAYERS["player_id"] == 6419].iloc[0]


def test_from_to_pandas():
    base = Base._from_pandas(pandas_base)
    assert isinstance(base, Base)
    for base_key, pandas_key in BASE_PANDAS_CONVERSION_MAP.items():
        assert base.__dict__[base_key] == pandas_base[pandas_key]
    pandas_base_2 = base._to_pandas()
    for key in PANDAS_BASE_CONVERSION_MAP.keys():
        assert pandas_base[key] == pandas_base_2[key]
