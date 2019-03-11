"""
This module provides an Initializer class that generates squads.
"""


class Initializer:
    """
    Initializes one or many squads.
    Args:
        formation: dict with formation information
        players: a pandas dataframe with all players
        compatible_players: a dict with position: dataframe with compatible players
        locked_players: a dict with position_id: player_id that must be used
    """

    def __init__(self, formation, players, compatible_players, locked_players):
        self.formation = formation
        self.players = players
        self.compatible_players = compatible_players
        self.locked_players = locked_players

    def _initialize(self):
        """
        Initializes a single squad.
        """
        squad = {}
        for slot_id in formation["positions"].keys():
            if self.locked_players is not None and \
                    slot_id in self.locked_players.keys():
                player = {
                    "data": self.players.loc[self.locked_players[slot_id]],
                    "is_locked": True
                }
            else:
                position = self.formation["positions"][slot_id]
                player = {
                    "data": self.compatible_players[position].sample().iloc[0],
                    "is_locked": False
                }
            squad[slot_id] = player
        return squad

    def initialize(self, n_squads=1):
        """
        Initializes a list of squads of size n_squads.
        If n_squads == 1, returns a squad object instead of a list.
        """
        if n_squads == 1:
            return self._initialize()
        else:
            return [self._initialize() for _ in range(n_squads)]
