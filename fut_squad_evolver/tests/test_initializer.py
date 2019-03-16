from fut_squad_evolver.nsga2.initializer import Initializer
from fut_squad_evolver.utils import data_loader


def test_initializer():
    formation = data_loader.FORMATIONS["442"]
    initializer = Initializer(
        formation,
        data_loader.PLAYERS,
        data_loader.COMPATIBLE_PLAYERS
    )
    squad = initializer.initialize()
    assert isinstance(squad, dict)
    assert len(squad) == len(formation["positions"])
    assert all(id in squad.keys() for id in range(len(squad)))
    assert all(isinstance(player, dict) for player in squad.values())


def test_initializer_locked():
    formation = data_loader.FORMATIONS["442"]
    locked_players = {0: 341}
    initializer = Initializer(
        formation,
        data_loader.PLAYERS,
        data_loader.COMPATIBLE_PLAYERS,
        locked_players
    )
    squad = initializer.initialize()
    assert isinstance(squad, dict)
    assert len(squad) == len(formation["positions"])
    assert all(id in squad.keys() for id in range(len(squad)))
    assert all(isinstance(player, dict) for player in squad.values())
    assert all(squad[key]["data"]["player_id"] == value for key, value in locked_players.items())


# from copy import deepcopy as copy
#
# from formation_calculations.calculate_chemistry import calculate_chemistry_position
# from utils.data_loader import PLAYERS
#
#
# ALL_POSITIONS = ["GK", "CB", "LB", "LWB", "RB", "RWB", "CDM",
#                  "CM", "CAM", "CF", "ST", "LM", "LW", "LF", "RM", "RW", "RF"]
# COMPATIBLE_POSITIONS = {position: [other_position for other_position in ALL_POSITIONS if calculate_chemistry_position(
#     position, other_position) >= 2] for position in ALL_POSITIONS}
# COMPATIBLE_PLAYERS = {position: PLAYERS[PLAYERS["position"].isin(
#     compatible_positions)] for position, compatible_positions in COMPATIBLE_POSITIONS.items()}
#
#
#
# from nsga2.initializer import initialize_squad, COMPATIBLE_PLAYERS
# from utils.data_loader import FORMATIONS
# formation = FORMATIONS["433"]
# my_squad = initialize_squad(formation, COMPATIBLE_PLAYERS)
# {key: {"name": value["data"]["player_extended_name"], "position": value["data"]["position"]} for key, value in my_squad.items()}
# locked_players = {2: 341}
# print("")
# my_squad = initialize_squad(formation, COMPATIBLE_PLAYERS, locked_players)
# {key: {"name": value["data"]["player_extended_name"], "position": value["data"]["position"]} for key, value in my_squad.items()}
#
