"""

"""
import pickle
import pandas as pd


PLAYERS = pd.read_pickle("../data/processed/ut_players.p")
with open("../data/processed/formations.p", "rb") as file_pointer:
    FORMATIONS = pickle.load(file_pointer)


def get_player_long(player_id):
    return PLAYERS.loc[player_id]


def get_player_short(player_id):
    return PLAYERS.loc[player_id][[
        "player_id", "player_name", "overall", "club", "league", "nationality",
        "position", "age", "pace", "dribbling", "shooting", "passing", "defending",
        "physicality", "base_id", "metal", "is_rare", "price"
    ]]


def get_base(base_id):
    return PLAYERS[PLAYERS["base_id"] == base_id][["base_id", "player_id"]]


def get_formation_ids():
    return list(FORMATIONS.keys())


def get_formation(formation_id):
    return FORMATIONS[formation_id]
