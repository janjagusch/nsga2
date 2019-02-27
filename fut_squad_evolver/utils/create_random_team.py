import pickle
import numpy as np
import pandas as pd

PLAYERS = pd.read_pickle("data/processed/ut_players.p")
with open("data/processed/formations.p", "rb") as file_pointer:
    FORMATIONS = pickle.load(file_pointer)


def create_random_team():
    k = np.random.choice(list(FORMATIONS.keys()))
    random_formation = FORMATIONS[k]
    random_formation["formation"] = k
    random_players = PLAYERS.sample(11)["player_id"]
    random_formation["player_ids"] = {i: p for i, p in enumerate(random_players)}
    return random_formation
