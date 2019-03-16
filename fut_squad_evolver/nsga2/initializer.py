"""
This module provides an Initializer class that generates squads.
"""


class Initializer:

    def __init__(self, formation, players, locked_players=None):
        self.formation = formation
        self.players = players
        if locked_players is None:
            locked_players = {}
        self.locked_players = locked_players

    def _initialize(self):
        """
        Initializes a single squad, needs to be overriden by the child class.
        """
        pass

    def initialize(self, n_squads=1):
        """
        Initializes a list of squads of size n_squads.
        If n_squads == 1, returns a squad object instead of a list.
        """
        if n_squads == 1:
            return self._initialize()
        else:
            return [self._initialize() for _ in range(n_squads)]


class CompatibilityInitializer:
    """
    Initializes one or many squads.
    Args:
        formation: dict with formation information
        players: a pandas dataframe with all players
        compatible_players: a dict with position: dataframe with compatible players
        locked_players: a dict with position_id: player_id that must be used
    """

    def __init__(self, formation, players, compatible_players, locked_players=None):
        super().__init__(formation, players, locked_players)
        self.compatible_players = compatible_players

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


INITIALIZER_MAP = {
    "CompatibilityInitializer": CompatibilityInitializer
}


def make_initializer(initializer_id, initializer_kwargs):
    if initializer_id not in INITIALIZER_MAP.keys():
        error = KeyError("initializer_id needs to be in {}.".format(INITIALIZER_MAP.keys()))
        raise error
    return INITIALIZER_MAP[initializer_id](**initializer_kwargs)
