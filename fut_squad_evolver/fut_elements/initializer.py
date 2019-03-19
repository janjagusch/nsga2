"""
This module provides an Initializer class that generates squads.
"""
from fut_squad_evolver.nsga2.initializer import Initializer
from fut_squad_evolver.fut_elements.calculate_chemistry import \
    make_compatible_players
from fut_squad_evolver.fut_elements.genotype import Squad
from fut_squad_evolver.fut_elements.player import Player
from fut_squad_evolver.fut_elements.slot import Slot


class SquadInitializer(Initializer):

    def __init__(self, n_squads, formation, players, locked_players=None):
        super().__init__(n_squads)
        self.formation = formation
        self.players = players
        if locked_players is None:
            locked_players = {}
        self.locked_players = locked_players


class CompatibilityInitializer(SquadInitializer):
    """
    Initializes one or many squads.
    Args:
        formation: dict with formation information
        players: a pandas dataframe with all players
        compatible_players: a dict with position: dataframe with compatible players
        locked_players: a dict with position_id: player_id that must be used
    """

    def __init__(self, n_squads, formation, players, min_compatibility, locked_players=None):
        super().__init__(n_squads, formation, players, locked_players)
        self.min_compatibility = min_compatibility
        self.compatible_players = make_compatible_players(self.players, self.min_compatibility)

    def _initialize(self):
        """
        Initializes a single squad.
        """
        slot_map = {}
        for slot_id in self.formation.positions.keys():
            if slot_id in self.locked_players.keys():
                player = Player._from_pandas(self.players.loc[self.locked_players[slot_id]])
                is_locked = True
            else:
                position = self.formation.positions[slot_id]
                player = Player._from_pandas(self.compatible_players[position].sample().iloc[0])
                is_locked = False
            slot = Slot(player, is_locked)
            slot_map[slot_id] = slot
        squad = Squad(slot_map, self.formation)
        return squad
