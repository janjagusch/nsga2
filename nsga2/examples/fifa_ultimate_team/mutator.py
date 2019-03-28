"""
This class implements the Mutation operator for the FUT example.
"""
import numpy as np
from nsga2.examples.fifa_ultimate_team.calculate_chemistry import make_compatible_players, calculate_chemistry_position
from nsga2.nsga2.mutator import Mutator


class SquadMutator(Mutator):

    def __init__(self, players, min_compatibility, mutation_probability, replace_probability, switch_probability, swap_probability):
        super().__init__(mutation_probability)
        self.players = players
        self.min_compatibility = min_compatibility
        self.compatible_players = make_compatible_players(
            players, min_compatibility)
        self.replace_probability = replace_probability
        self.switch_probability = switch_probability
        self.swap_probability = swap_probability

    def _replace_mutate_id(self, genotype, replace_slot_id):
        slot_map = genotype.slot_map
        replace_position = genotype.formation.positions[replace_slot_id]
        # Only apply mutation if slot is not locked.
        if not slot_map[replace_slot_id].is_locked:
            other_slot_ids = [
                slot_id for slot_id in genotype.slot_map.keys() if slot_id != replace_slot_id]
            other_base_ids = [
                slot_map[slot_id].player.base_id for slot_id in other_slot_ids]
            compatible_players_position = self.compatible_players[replace_position]
            slot_map[replace_slot_id].player =\
                compatible_players_position[~compatible_players_position["base_id"].isin(
                    other_base_ids)].sample().iloc[0]["player"]

    def _replace_mutate(self, genotype):
        slot_map = genotype.slot_map
        replace_slot_id = np.random.choice(list(slot_map.keys()))
        self._replace_mutate_id(genotype, replace_slot_id)

    def _switch_mutate_id(self, genotype, switch_slot_id):
        slot_map = genotype.slot_map
        if not slot_map[switch_slot_id].is_locked:
            replace_base_id = slot_map[switch_slot_id].player.base_id
            players = self.players
            slot_map[switch_slot_id].player = players[players["base_id"] == replace_base_id].sample().iloc[0].player

    def _switch_mutate(self, genotype):
        slot_map = genotype.slot_map
        switch_slot_id = np.random.choice(list(slot_map.keys()))
        self._replace_mutate_id(genotype, switch_slot_id)

    def _swap_mutate_id(self, genotype, swap_slot_id):
        slot_map = genotype.slot_map
        swap_position = genotype.formation.positions[swap_slot_id]
        compatible_slots = [slot_id for slot_id, position in genotype.formation.positions.items() if calculate_chemistry_position(swap_position, position) >= self.min_compatibility]
        other_slot = np.random.choice(compatible_slots)
        if not slot_map[swap_slot_id].is_locked and not slot_map[other_slot].is_locked:
            player_a = slot_map[swap_slot_id].player
            player_b = slot_map[other_slot].player
            slot_map[swap_slot_id].player = player_b
            slot_map[other_slot].player = player_a

    def _swap_mutate(self, genotype):
        slot_map = genotype.slot_map
        swap_slot_id = np.random.choice(list(slot_map.keys()))
        self._replace_mutate_id(genotype, swap_slot_id)

    def mutate(self, individual):
        genotype = individual.genotype
        mutator = np.random.choice([self._replace_mutate, self._switch_mutate, self._swap_mutate], p=[self.replace_probability, self.switch_probability, self.swap_probability])
        mutator(genotype)
