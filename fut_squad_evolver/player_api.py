"""

"""

import pandas as pd


PLAYERS = pd.read_pickle("../data/processed/ut_players.p")


def get_player_long(player_id):
    player_id = int(player_id)
    return PLAYERS.loc[player_id].to_json()


def get_player_short(player_id):
    player_id = int(player_id)    
    return PLAYERS.loc[player_id][[
        "player_id", "player_name", "overall", "club", "league", "nationality",
        "position", "age", "pace", "dribbling", "shooting", "passing", "defending",
        "physicality", "base_id", "metal", "is_rare", "price"
    ]].to_json()
