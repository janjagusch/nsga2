import pickle
import pandas as pd


PLAYERS = pd.read_pickle("data/processed/ut_players.p")
with open("data/processed/formations.p", "rb") as file_pointer:
    FORMATIONS = pickle.load(file_pointer)
