"""
This class describes a squad - a team of players.
"""
import numpy as np

from fut_squad_evolver.fut_elements.calculate_chemistry import calculate_chemistry_position, \
    calculate_inter_player_chemistry, calculate_individual_chemistry, calculate_chemistry
from fut_squad_evolver.nsga2.genotype import Genotype


class Squad(Genotype):

    def __init__(self, slot_map, formation):
        self.slot_map = slot_map
        self.formation = formation

    def evaluate(self):
        """
        Evaluates the squad provided a self.formation and returns overall, price and
        chemistry.
        """
        evaluation = {
            "price": self._evalulate_price(),
            "overall": self._evalulate_overall(),
            "chemistry": self._evalulate_chemistry()
        }
        return evaluation

    def _evalulate_price(self):
        return np.sum([slot.player.price for slot in self.slot_map.values()])

    def _evalulate_overall(self):
        return np.mean([slot.player.overall for slot in self.slot_map.values()])

    def _evalulate_chemistry(self):
        sum_chemistry = 0
        for key, slot in self.slot_map.items():
            player = slot.player
            # calculate position chemistry
            player_position = player.position
            formation_position = self.formation.positions[key]
            position_chemistry = calculate_chemistry_position(
                player_position, formation_position)
            # calculate linked player chemistry
            linked_players = [self.slot_map[k].player for k in self.formation.links[key]]
            link_sum = np.sum([calculate_inter_player_chemistry(player, other_player) for other_player in linked_players])
            link_chemistry = calculate_individual_chemistry(link_sum, len(linked_players))
            # calculate total chemistry
            sum_chemistry += calculate_chemistry(link_chemistry, position_chemistry)
        # truncate chemistry at maximum value
        if sum_chemistry > 100:
            sum_chemistry = 100
        return sum_chemistry

    def __repr__(self):
        repr = "{}(slot_map={})".format(self.__class__.__name__, self.slot_map)
        return repr

    def __str__(self):
        label_map = {key: label for key, label in self.formation.labels.items()}
        player_map = {key: slot.player for key, slot in self.slot_map.items()}
        squad_str = ""
        for slot_id, slot_label in label_map.items():
            player = player_map[slot_id]
            squad_str += "{}:\tPlayer(id={}, name={}, club={}, league={}, nationality={}, position={}, overall={}, price={})\n".format(slot_label, player.player_id, player.base.name, player.club, player.league, player.nationality, player.position, player.overall, player.price)
        return squad_str
