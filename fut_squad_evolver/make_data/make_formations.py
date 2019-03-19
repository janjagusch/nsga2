from fut_squad_evolver.fut_elements.formation import Formation


def process_formations(formations_json):
    formations_processed = {key: Formation(**value)
                            for key, value in formations_json.items()}
    return formations_processed
