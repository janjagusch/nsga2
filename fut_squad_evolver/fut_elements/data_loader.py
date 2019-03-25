"""
Loads all files.
"""
import pickle

import pandas as pd

from fut_squad_evolver.utils.read_write import read_file


PLAYERS = read_file("data/processed", "ut_players.p")


FORMATIONS = read_file("data/processed", "formations.p")
