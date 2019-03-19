from fut_squad_evolver.fut_elements.data_loader import FORMATIONS, PLAYERS
from fut_squad_evolver.fut_elements.genotype import Squad
from fut_squad_evolver.fut_elements.initializer import CompatibilityInitializer
from fut_squad_evolver.nsga2.individual import Individual
from fut_squad_evolver.nsga2.initializer import Initializer


def test_is_subclass():
    assert issubclass(CompatibilityInitializer, Initializer)


def test_constructor():
    n_squads = 10
    formation = FORMATIONS["442"]
    players = PLAYERS
    min_compatibility = 2
    locked_players = {}
    initializer = CompatibilityInitializer(
        n_squads, formation, players, min_compatibility, locked_players)


def test_initializer_no_lock():
    n_squads = 10
    formation = FORMATIONS["442"]
    players = PLAYERS
    min_compatibility = 2
    locked_players = {}
    initializer = CompatibilityInitializer(
        n_squads, formation, players, min_compatibility, locked_players)
    population = initializer.initialize()
    assert isinstance(population, list)
    assert len(population) == n_squads
    for indiviual_id, individual in population.items():
        assert isinstance(individual, Individual)
        assert isinstance(individual.genotype, Squad)
        for slot in individual.genotype.slot_map.values():
            assert not slot.is_locked


def test_initializer_no_lock():
    n_squads = 1
    formation = FORMATIONS["442"]
    players = PLAYERS
    min_compatibility = 2
    # TODO: make formation slot_ids int
    slot_id = "5"
    player_id = 341
    locked_players = {slot_id: player_id}
    initializer = CompatibilityInitializer(
        n_squads, formation, players, min_compatibility, locked_players)
    population = initializer.initialize()
    assert population[0].genotype.slot_map[slot_id].player.player_id == player_id
    assert population[0].genotype.slot_map[slot_id].is_locked
