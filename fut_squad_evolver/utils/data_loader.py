import pickle
import pandas as pd


PLAYERS = pd.read_pickle("../data/processed/ut_players.p")
with open("../data/processed/formations.p", "rb") as file_pointer:
    FORMATIONS = pickle.load(file_pointer)
POSITIONS = ["GK", "CB", "LB", "LWB", "RB", "RWB", "CDM",
             "CM", "CAM", "CF", "ST", "LM", "LW", "LF", "RM", "RW", "RF"]


def make_compatible_players(players, min_compatibility):
    compatible_positions = {position: [other_position for other_position in POSITIONS
                                       if calculate_chemistry_position(
                                           position, other_position) >= 2] for position in ALL_POSITIONS}


COMPATIBLE_PLAYERS = {position: PLAYERS[PLAYERS["position"].isin(
    compatible_positions)] for position, compatible_positions in COMPATIBLE_POSITIONS.items()}
