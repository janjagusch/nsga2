"""

"""
import numpy as np
from fut_squad_evolver.formation_calculations import calculate_chemistry
from fut_squad_evolver.utils.data_loader import PLAYERS


def _calculate_sum_price(formation):
    """
    Calculates the sum of all players' prices (on PS4).
    """
    return np.sum([player["price"] for player in formation["players"].values()])


def _calculate_avg_rating(formation):
    """
    Calculates the average of all players' rating.
    """
    return np.mean([player["overall"] for player in formation["players"].values()])


def _calculate_sum_chemistry(formation):
    """
    Calculates the sum of all player's chemistry.
    """
    sum_chemistry = 0
    for slot_id, player in formation["players"].items():
        player_position = player["position"]
        squad_position = formation["positions"][slot_id]
        position_chemistry = \
            calculate_chemistry.calculate_chemistry_position(
                player_position, squad_position)
        linked_players = \
            [formation["players"][player_id]
                for player_id in formation["links"][slot_id]]
        link_sum = \
            np.sum([calculate_chemistry.
                    calculate_inter_player_chemistry(player, other_player)
                    for other_player in linked_players])
        link_chemistry = \
            calculate_chemistry.calculate_individual_chemistry(
                link_sum, len(linked_players))
        player_chemistry = \
            calculate_chemistry.calculate_chemistry(
                link_chemistry, position_chemistry)
        sum_chemistry += player_chemistry
    if sum_chemistry > 100:
        sum_chemistry = 100
    return sum_chemistry


def calculate_metrics(formation):
    """
    Calculates average rating, sum of price and sum of chemistry for formation.
    """
    metrics = {}
    formation["players"] = {key: PLAYERS.loc[value].to_dict()
                            for key, value in formation["player_ids"].items()}
    metrics["price"] = _calculate_sum_price(formation)
    metrics["rating"] = _calculate_avg_rating(formation)
    metrics["chemistry"] = _calculate_sum_chemistry(formation)
    return metrics
