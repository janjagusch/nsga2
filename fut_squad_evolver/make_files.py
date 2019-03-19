from fut_squad_evolver.utils.read_write import read_file, write_file
from fut_squad_evolver.make_data.make_formations import process_formations


def make_files():

    RAW_DIRECTORY = "data/raw"
    PROCESSED_DIRECTORY = "data/processed"
    # process formations
    formations_json = read_file(RAW_DIRECTORY, "formations.json")
    formations_processed = process_formations(formations_json)
    write_file(formations_processed, PROCESSED_DIRECTORY, "formations.p")
