from formation import Formation


def make_formations(formations_json):
    formations_processed = {key: Formation(**value)
                            for key, value in formations_json.items()}
    return formations_processed
