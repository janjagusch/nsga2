import pickle
from fut_squad_evolver.make_data import formations_raw as formations

intermediate_reversed = {formation: {id: position for position, id in value.items(
)} for formation, value in formations.intermediate.items()}

position_cleaned = {key: value["pos"]
                    for key, value in formations.position.items()}

position_str = {formation: {key: position_cleaned[formation][val - 1] for key,
                            val in value.items()} for formation, value in formations.intermediate.items()}

intermediate_cleaned = {formation: {key: val - 1 for key, val in value.items()}
                        for formation, value in formations.intermediate.items()}

position_final = {formation: {intermediate_cleaned[formation][key]: val for key, val in value.items(
)} for formation, value in position_str.items()}

links_str = dict()
for formation, value in formations.link.items():
    old_keys = value["draw"].keys()
    old_values = value["draw"].values()
    new_keys = [k if isinstance(
        k, str) else intermediate_reversed[formation][k] for k in old_keys]
    new_values = [[v if isinstance(
        v, str) else intermediate_reversed[formation][v] for v in val] for val in old_values]
    links_str[formation] = {k: v for k, v in zip(new_keys, new_values)}

links_final = {formation: {intermediate_cleaned[formation][key]: [
    intermediate_cleaned[formation][v] for v in val] for key, val in value.items()} for formation, value in links_str.items()}

labels_final = {formation: {key - 1: val for key, val in value.items()}
                for formation, value in intermediate_reversed.items()}

formation_final = {}
for formation in position_final.keys():
    formation_final[formation] = {}
    formation_final[formation]["positions"] = position_final[formation]
    formation_final[formation]["links"] = links_final[formation]
    formation_final[formation]["labels"] = labels_final[formation]


with open("data/processed/formations.p", "wb") as file_pointer:
    pickle.dump(formation_final, file_pointer)
