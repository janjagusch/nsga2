import numpy as np

from fut_squad_evolver.fut_elements.crossover import SquadCrossover
from fut_squad_evolver.fut_elements.genotype import Squad
from fut_squad_evolver.nsga2.individual import Individual
from fut_squad_evolver.fut_elements.data_loader import PLAYERS, FORMATIONS
from fut_squad_evolver.fut_elements.initializer import CompatibilityInitializer

def test_copy_genotype():
    initializer = CompatibilityInitializer(2, FORMATIONS["442"], PLAYERS, 2)
    genotype_a = initializer._initialize()
    genotype_b = initializer._initialize()

    crossover = SquadCrossover(0.05)
    child_genotype_a, child_genotype_b = crossover._copy_genotype(genotype_a, genotype_b)
    assert child_genotype_a is not genotype_a
    assert child_genotype_b is not genotype_b
    assert child_genotype_a.formation is genotype_a.formation
    assert child_genotype_b.formation is genotype_b.formation
    for slot_id, slot in child_genotype_a.slot_map.items():
        assert slot is not genotype_a.slot_map[slot_id]
        assert slot.player is genotype_a.slot_map[slot_id].player
        assert slot.is_locked == genotype_a.slot_map[slot_id].is_locked
    for slot_id, slot in child_genotype_b.slot_map.items():
        assert slot is not genotype_b.slot_map[slot_id]
        assert slot.player is genotype_b.slot_map[slot_id].player
        assert slot.is_locked == genotype_b.slot_map[slot_id].is_locked


def test_swap_slots():
    np.random.seed(25051994)
    formation = FORMATIONS["442"]
    initializer = CompatibilityInitializer(2, formation, PLAYERS, 2)
    genotype_a = initializer._initialize()
    genotype_b = initializer._initialize()
    crossover = SquadCrossover(0.05)
    swap_slot_id = 5
    swap_slot_ids = [swap_slot_id] + formation.links[swap_slot_id]
    print(swap_slot_ids)
    child_genotype_a, child_genotype_b = crossover._swap_slots(genotype_a, genotype_b, swap_slot_id)
    assert child_genotype_a is not genotype_a
    assert child_genotype_b is not genotype_b
    assert child_genotype_a.formation is genotype_a.formation
    assert child_genotype_b.formation is genotype_b.formation
    for slot_id, slot in child_genotype_a.slot_map.items():
        assert slot is not genotype_a.slot_map[slot_id]
        if slot_id in swap_slot_ids:
            assert slot.player is genotype_b.slot_map[slot_id].player
        else:
            assert slot.player is genotype_a.slot_map[slot_id].player
            assert slot.is_locked == genotype_a.slot_map[slot_id].is_locked
    for slot_id, slot in child_genotype_b.slot_map.items():
        assert slot is not genotype_b.slot_map[slot_id]
        if slot_id in swap_slot_ids:
            assert slot.player is genotype_a.slot_map[slot_id].player
        else:
            assert slot.player is genotype_b.slot_map[slot_id].player
            assert slot.is_locked == genotype_b.slot_map[slot_id].is_locked


def test_swap_slots_locked():
    np.random.seed(25051994)
    locked_players = {5: 341}
    formation = FORMATIONS["442"]
    initializer = CompatibilityInitializer(2, formation, PLAYERS, 2, locked_players)
    genotype_a = initializer._initialize()
    genotype_b = initializer._initialize()
    crossover = SquadCrossover(0.05)
    swap_slot_id = 5
    swap_slot_ids = [swap_slot_id] + formation.links[swap_slot_id]
    print(swap_slot_ids)
    child_genotype_a, child_genotype_b = crossover._swap_slots(genotype_a, genotype_b, swap_slot_id)
    assert child_genotype_a is not genotype_a
    assert child_genotype_b is not genotype_b
    assert child_genotype_a.formation is genotype_a.formation
    assert child_genotype_b.formation is genotype_b.formation
    for slot_id, slot in child_genotype_a.slot_map.items():
        assert slot is not genotype_a.slot_map[slot_id]
        if slot_id in swap_slot_ids and slot_id not in locked_players.keys():
            assert slot.player is genotype_b.slot_map[slot_id].player
        else:
            assert slot.player is genotype_a.slot_map[slot_id].player
            assert slot.is_locked == genotype_a.slot_map[slot_id].is_locked
    for slot_id, slot in child_genotype_b.slot_map.items():
        assert slot is not genotype_b.slot_map[slot_id]
        if slot_id in swap_slot_ids and slot_id not in locked_players.keys():
            assert slot.player is genotype_a.slot_map[slot_id].player
        else:
            assert slot.player is genotype_b.slot_map[slot_id].player
            assert slot.is_locked == genotype_b.slot_map[slot_id].is_locked


def test_crossover():
    np.random.seed(25051994)
    formation = FORMATIONS["442"]
    initializer = CompatibilityInitializer(2, formation, PLAYERS, 2)
    individual_a = initializer._initialize_individual()
    individual_b = initializer._initialize_individual()
    crossover = SquadCrossover(1)
    child_a, child_b = crossover.crossover(individual_a, individual_b)
    assert isinstance(child_a, Individual)
    assert isinstance(child_b, Individual)
    assert isinstance(child_a.genotype, Squad)
    assert isinstance(child_b.genotype, Squad)
    assert child_a is not individual_a
    assert child_b is not individual_b
    assert child_a.genotype is not individual_a.genotype
    assert child_b.genotype is not individual_b.genotype
    crossover = SquadCrossover(0)
    child_a, child_b = crossover.crossover(individual_a, individual_b)
    assert isinstance(child_a, Individual)
    assert isinstance(child_b, Individual)
    assert isinstance(child_a.genotype, Squad)
    assert isinstance(child_b.genotype, Squad)
    assert child_a is not individual_a
    assert child_b is not individual_b
    assert child_a.genotype is not individual_a.genotype
    assert child_b.genotype is not individual_b.genotype
