"""
The Crossover operator for the FUT example.
"""
from copy import copy

import numpy as np

from nsga2.nsga2.crossover import Crossover
from nsga2.examples.fifa_ultimate_team.genotype import Squad
from nsga2.examples.fifa_ultimate_team.slot import Slot


class SquadCrossover(Crossover):

    def __init__(self, crossover_probability):
        super().__init__(crossover_probability)

    def _copy_genotype(self, genotype_a, genotype_b):
        slot_map_a = {slot_id: copy(slot) for slot_id, slot in genotype_a.slot_map.items()}
        slot_map_b = {slot_id: copy(slot) for slot_id, slot in genotype_b.slot_map.items()}
        return Squad(slot_map_a, genotype_a.formation), Squad(slot_map_b, genotype_b.formation)

    def _swap_slots(self, genotype_a, genotype_b, swap_slot_id):
        slot_map_a = {}
        slot_map_b = {}
        swap_slots = [swap_slot_id] + genotype_a.formation.links[swap_slot_id]
        not_swap_slots = [slot_id for slot_id in genotype_a.formation.links.keys() if slot_id not in swap_slots]
        not_swap_base_ids_a = [genotype_a.slot_map[slot_id].player.base_id for slot_id in not_swap_slots]
        not_swap_base_ids_b = [genotype_b.slot_map[slot_id].player.base_id for slot_id in not_swap_slots]
        swap_slots_new = []
        for slot_id in swap_slots:
            if genotype_a.slot_map[slot_id].player.base_id in not_swap_base_ids_b:
                pass
            if genotype_b.slot_map[slot_id].player.base_id in not_swap_base_ids_a:
                pass
            swap_slots_new.append(slot_id)
        for slot_id in genotype_a.slot_map.keys():
            if slot_id in swap_slots_new and not genotype_a.slot_map[slot_id].is_locked:
                slot_map_a[slot_id] = Slot(genotype_b.slot_map[slot_id].player, genotype_b.formation)
                slot_map_b[slot_id] = Slot(genotype_a.slot_map[slot_id].player, genotype_a.formation)
            else:
                slot_map_a[slot_id] = copy(genotype_a.slot_map[slot_id])
                slot_map_b[slot_id] = copy(genotype_b.slot_map[slot_id])
        return Squad(slot_map_a, genotype_a.formation), Squad(slot_map_b, genotype_b.formation)

    def _crossover_genotype(self, genotype_a, genotype_b):
        random_slot_id = np.random.choice(list(genotype_a.slot_map.keys()))
        return self._swap_slots(genotype_a, genotype_b, random_slot_id)
