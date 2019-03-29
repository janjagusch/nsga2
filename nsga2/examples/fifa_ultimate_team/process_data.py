"""
This module helps you to recreate the files needed to this project.
"""
from io import BytesIO
from zipfile import ZipFile
import os

import pandas as pd

from nsga2.examples.fifa_ultimate_team.make_data.make_players import make_players
from nsga2.examples.fifa_ultimate_team.make_data.make_formations import make_formations

from nsga2.examples.fifa_ultimate_team.read_write import read_file, write_file


def load_dataset_from_kaggle():
    """
    Downloads the dataset from Kaggle and places the .zip file in data/external.
    """
    cmd = "kaggle datasets download -d stefanoleone992/fifa-19-fifa-ultimate-team -p data/external"
    os.system(cmd)


def read_dataset_from_zip():
    with ZipFile("data/external/fifa-19-fifa-ultimate-team.zip") as archive:
        file = archive.read("FIFA19 - Ultimate Team players.xlsx")
        file = BytesIO(file)
        dataset = pd.read_excel(file)
    dataset.to_pickle("data/interim/players.p")
    return dataset


def process_formations():
    formations = read_file("nsga2/examples/fifa_ultimate_team/data/raw", "formations.json")
    formations = make_formations(formations)
    write_file(formations, "nsga2/examples/fifa_ultimate_team/data/processed", "formations.p")
    return formations


def process_players():
    players = read_file("nsga2/examples/fifa_ultimate_team/data/interim", "players.p")\
        .sort_values(["base_id", "player_id"])
    players["metal"] = players["quality"]\
        .str.split(" - ").apply(lambda x: x[0])
    players["is_rare"] = players["quality"]\
        .str.split(" - ").apply(lambda x: len(x) == 2)
    players["price"] = players["ps4_last"]
    players = players.set_index("player_id", drop=False)
    players = make_players(players)
    write_file(players, "nsga2/examples/fifa_ultimate_team/data/processed", "players.p")
    return players
