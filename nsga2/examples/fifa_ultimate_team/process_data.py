"""
This module helps you to recreate the files needed to this project.
"""
from io import BytesIO
from zipfile import ZipFile
import os

import pandas as pd

from make_data.make_players import make_players
from make_data.make_formations import make_formations

from read_write import read_file, write_file

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



def process_players():
    dataset = pd.read_pickle(
        "data/interim/players.p").sort_values(["base_id", "player_id"])
    dataset["metal"] = dataset["quality"]\
        .str.split(" - ").apply(lambda x: x[0])
    dataset["is_rare"] = dataset["quality"]\
        .str.split(" - ").apply(lambda x: len(x) == 2)
    dataset["price"] = dataset["ps4_last"]
    dataset = dataset.set_index("player_id", drop=False)
    dataset = make_players(dataset)
    dataset.to_pickle("data/processed/players.p")
    return dataset
