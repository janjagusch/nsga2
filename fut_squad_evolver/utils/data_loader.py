import pickle
import pandas as pd


PLAYERS = pd.read_pickle("../data/processed/ut_players.p")
with open("../data/processed/formations.p", "rb") as file_pointer:
    FORMATIONS = pickle.load(file_pointer)
POSITIONS = ["GK", "CB", "LB", "LWB", "RB", "RWB", "CDM",
             "CM", "CAM", "CF", "ST", "LM", "LW", "LF", "RM", "RW", "RF"]





COMPATIBLE_PLAYERS = {position: PLAYERS[PLAYERS["position"].isin(
    compatible_positions)] for position, compatible_positions in COMPATIBLE_POSITIONS.items()}
