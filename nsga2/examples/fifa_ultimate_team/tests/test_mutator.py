from fut_squad_evolver.fut_elements.mutator import SquadMutator
from fut_squad_evolver.fut_elements.initializer import CompatibilityInitializer
from fut_squad_evolver.fut_elements import data_loader
from fut_squad_evolver.nsga2.individual import Individual


def test_replace_mutate_id():
    formation = data_loader.FORMATIONS["442"]
    players = data_loader.PLAYERS
    initializer = CompatibilityInitializer(1, formation, players, 2)
    genotype = initializer._initialize()
    slot_id = 5
    player = genotype.slot_map[slot_id].player
    mutator = SquadMutator(players, 2, 1, 0.5, 0.3, 0.2)
    mutator._replace_mutate_id(genotype, slot_id)
    new_player = genotype.slot_map[slot_id].player
    assert player is not new_player


def test_switch_mutate_id():
    formation = data_loader.FORMATIONS["442"]
    players = data_loader.PLAYERS
    locked_players = {5: 341}
    initializer = CompatibilityInitializer(1, formation, players, 2, locked_players)
    genotype = initializer._initialize()
    slot_id = 5
    genotype.slot_map[slot_id].is_locked = False
    player = genotype.slot_map[slot_id].player
    mutator = SquadMutator(players, 2, 1, 0.5, 0.3, 0.2)
    success = False
    for i in range(100):
        mutator._switch_mutate_id(genotype, slot_id)
        new_player = genotype.slot_map[slot_id].player
        if player is not new_player:
            success = True
            break
    assert success


def test_swap_mutate_id():
    formation = data_loader.FORMATIONS["442"]
    players = data_loader.PLAYERS
    initializer = CompatibilityInitializer(1, formation, players, 2)
    genotype = initializer._initialize()
    slot_id = 4
    player = genotype.slot_map[slot_id].player
    mutator = SquadMutator(players, 2, 1, 0.5, 0.3, 0.2)
    success = False
    for i in range(100):
        mutator._swap_mutate_id(genotype, slot_id)
        new_player = genotype.slot_map[slot_id].player
        if player is not new_player:
            success = True
            break
    assert success


def test_mutate():
    formation = data_loader.FORMATIONS["442"]
    players = data_loader.PLAYERS
    initializer = CompatibilityInitializer(1, formation, players, 2)
    individual = initializer._initialize_individual()
    mutator = SquadMutator(players, 2, 1, 0.5, 0.3, 0.2)
    mutator.mutate(individual)
    assert isinstance(individual, Individual)
