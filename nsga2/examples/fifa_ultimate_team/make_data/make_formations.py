from nsga2.examples.fifa_ultimate_team.formation import Formation


def make_formations(formations_json):
    for formation in formations_json.values():
        positions_new = {}
        for key, value in formation["positions"].items():
            positions_new[int(key)] = value
        formation["positions"] = positions_new
        links_new = {}
        for key, value in formation["links"].items():
            links_new[int(key)] = value
        formation["links"] = links_new
        labels_new = {}
        for key, value in formation["labels"].items():
            labels_new[int(key)] = value
        formation["labels"] = labels_new
    formations_processed = {key: Formation(**value)
                            for key, value in formations_json.items()}
    return formations_processed
