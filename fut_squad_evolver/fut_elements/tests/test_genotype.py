import numpy as np

from fut_squad_evolver.fut_elements.data_loader import PLAYERS, FORMATIONS
from fut_squad_evolver.fut_elements.genotype import Squad
from fut_squad_evolver.fut_elements.player import Player
from fut_squad_evolver.fut_elements.slot import Slot
from fut_squad_evolver.nsga2.genotype import Genotype


def test_is_subclass():
    assert issubclass(Squad, Genotype)

def test_constructor():
    slot_map = {
        i: Slot(Player._from_pandas(PLAYERS.sample().iloc[0]), False)
        for i in range(11)
    }
    formation = FORMATIONS["442"]
    squad = Squad(slot_map, formation)

def test_evaluate():
    slot_map = {
        i: Slot(Player._from_pandas(PLAYERS.sample().iloc[0]), False)
        for i in range(11)
    }
    formation = FORMATIONS["442"]
    squad = Squad(slot_map, formation)
    phenotype = squad.evaluate()
    assert isinstance(phenotype, dict)
    for value in phenotype.values():
        assert isinstance(value, (int, float, np.int64))
