import warnings
import copy
import pandas as pd
import numpy as np


# all possible positions in a formation.
_POSITIONS = ["GK", 
              "RB", "CB", "LB", "LWB", "RWB",
              "CDM", "CM", "CAM", "RM", "LM",
              "RW", "LW", "CF", "RF", "LF", "ST"
             ]


# chemistry between two positions (bi-directional).
_POSITION_CHEMISTRY = {
    ("CB", "RB"): 1,
    ("LB", "RB"): 1,
    ("LB", "CB"): 1,
    ("RWB", "RB"): 2,
    ("LWB", "LB"): 2,
    ("LWB", "RWB"): 1,
    ("CDM", "CB"): 1,
    ("CM", "CDM"): 2,
    ("CAM", "CDM"): 1,
    ("CAM", "CM"): 2,
    ("RM", "RB"): 1,
    ("RM", "RWB"): 1,
    ("RM", "CM"): 1,
    ("LM", "LB"): 1,
    ("LM", "LWB"): 1,
    ("LM", "CM"): 1,
    ("LM", "RM"): 1,
    ("RW", "RB"): 1,
    ("RW", "RWB"): 1,
    ("RW", "RM"): 2,
    ("LW", "LB"): 1,
    ("LW", "LWB"): 1,
    ("LW", "LM"): 2,
    ("LW", "RW"): 1,
    ("CF", "CAM"): 2,
    ("RF", "RM"): 1,
    ("RF", "RW"): 2,
    ("RF", "CF"): 1,
    ("LF", "LM"): 1,
    ("LF", "LW"): 2,
    ("LF", "CF"): 1,
    ("LF", "RF"): 1,
    ("ST", "CF"): 2,
    ("CF", "RF"): 1,
    ("CF", "LF"): 1    
}


# returns chemistry between two positions.
def _get_position_chemistry(position_1, position_2):
    if position_1 not in _POSITIONS or position_2 not in _POSITIONS:
        raise IndexError
    if position_1 == position_2:
        return 3
    if (position_1, position_2) in _POSITION_CHEMISTRY.keys():
        return _POSITION_CHEMISTRY[(position_1, position_2)]
    if (position_2, position_1) in _POSITION_CHEMISTRY.keys():
        return _POSITION_CHEMISTRY[(position_2, position_1)]
    return 0


class Position:
    
    def __init__(self, id):
        self.id = id
        
    def get_chemistry(self, other):
        return _get_position_chemistry(self.id, other.id)
    
    def get_compatible_positions(self, min_chemistry=2):
        compatible_positions = []
        for position in POSITIONS.values():
            if self.get_chemistry(position) >= min_chemistry:
                compatible_positions.append(position)
        return compatible_positions
    
    def __repr__(self):
        return "{}(id={})".format(self.__class__.__name__, self.id)

    
POSITIONS = {p: Position(p) for p in _POSITIONS}

    
def get_positions():
    return POSITIONS  

    
def get_position(position):
    return POSITIONS[position]


with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    players = pd.read_csv("../input/FIFA19 - Ultimate Team players.csv")

condition = ~players.price_ps4.isna()
players = players[condition].reset_index()
players.columns = players.columns.str.lower()


class Player:
    
    def __init__(self, data):
        """
        Creates Player instance.
        Args:
            data: a Pandas series from the players dataframe.
        Returns:
            a Player instance.
        """
        self.data = data
        self.position = get_position(self.data.position)
        
    def __eq__(self, other):
        """
        Checks for equality between self and other.
        One player can have several card versions, so only matching the player_id is not sufficient.
        Args:
            other: a Player instance.
        Returns:
            a boolean, indicating equality between self and other.
        """
        if self.data.player_extended_name != other.data.player_extended_name:
            return False
        if self.data.date_of_birth != other.data.date_of_birth:
            return False
        return True
    
    def get_chemistry(self, other):
        """
        Calculates chemistry to other.
        Args:
            other: a Player instance.
        Returns:
            an integer, representing the chemistry between self and other.
        """
        chemistry = 0
        if self.data.nationality == other.data.nationality:
            chemistry += 1
        if self.data.league == other.data.league:
            chemistry += 1
        if self.data.club == other.data.club:
            chemistry += 1
        return chemistry
    
    def __repr__(self):
        return "{}(id={}, name={}, overall={}, position={}, price={}, nationality={}, league={}, club={})".format(self.__class__.__name__, self.data.player_id, 
                                                                                                                  self.data.player_name, self.data.overall,
                                                                                                                  self.position.id, int(self.data.price_ps4),
                                                                                                                  self.data.nationality, self.data.league, self.data.club)


players = players.apply(lambda x: Player(x.copy()), axis=1)


class Link:
    
    def __init__(self, slot_1, slot_2):
        """
        Creates Link instance.
        Args:
            slot_1: an instance of Slot.
            slot_2: an instance of Slot.
        Returns:
            an instance of Link.
        """
        self.slot_1 = slot_1
        self.slot_2 = slot_2
        slot_1.links.append(self)
        slot_2.links.append(self)
        
    def get_other(self, slot):
        """
        Get partner of slot.
        Args:
            slot: an instance of Slot.
        Returns:
            an instance of Slot.
        Raise:
            IndexError, when slot not slot_1 and slot not slot_2.
        """
        if slot is self.slot_1:
            return self.slot_2
        if slot is self.slot_2:
            return self.slot_1
        raise IndexError
        
    def get_chemistry(self):
        return self.slot_1.player.get_chemistry(self.slot_2.player)
        
    def __repr__(self):
        return "{}(slot_1={}, slot_2={})".format(self.__class__.__name__, self.slot_1.slot_id, self.slot_2.slot_id)

    
def make_links(links, slots):
    """Converts links dictionary to Link instances."""
    return [Link(slots[p1], slots[p2]) for p1, p2 in links]


class Slot:
    
    def __init__(self, slot_id, position, player=None, links=None):
        """
        Creates Slot instance.
        Args:
            slot_id: string sequence.
            position: instance of Position.
            player: instance of Player.
            links: list of Link instances.
        Returns:
            instance of Slot.
        """
        self.slot_id = slot_id
        self.position = position
        self.player = player
        if links is None:
            links = []
        self.links = links
        
    def __repr__(self):
        return "{}(id={}, position={}, player={})".format(self.__class__.__name__, self.slot_id, self.position, self.player)
    
    def get_linked_slots(self):
        """Return all slots that this slot is linked to."""
        return [l.get_other(self) for l in self.links]
    
    def get_linked_players(self):
        """Return all players that this slot is linked to."""
        return [s.player for s in self.get_linked_slots()]
    
    def get_position_chemistry(self):
        """Get chemistry between natural position of player and position of slot."""        
        return self.position.get_chemistry(self.player.position)
    
    def get_link_chemistry(self):
        """Get chemistry between player in slot and players in linked slots."""
        return np.mean([self.player.get_chemistry(p) for p in self.get_linked_players()])
    
    def get_chemistry(self):
        """Get overall chemistry, given link chemistry and position chemistry."""
        return get_chemistry(self.get_link_chemistry(), self.get_position_chemistry())

    
def get_chemistry(link_chemistry, position_chemistry):
    """
    Calculates individal slot chemistry, given link chemistry and position chemistry.
    Args:
        link_chemistry: float value.
        position_chemistry: int value.
    Returns:
        a float value.
    Raises:
        IndexError, when link_chemistry or position_chemistry not within boundaries.
    """
    if link_chemistry < 0.3:
        if position_chemistry == 0:
            return 0
        if position_chemistry == 1:
            return 1
        if position_chemistry == 2:
            return 2
        if position_chemistry == 3:
            return 3
        raise IndexError
    if link_chemistry < 1.:
        if position_chemistry == 0:
            return 1
        if position_chemistry == 1:
            return 3
        if position_chemistry == 2:
            return 5
        if position_chemistry == 3:
            return 6
        raise IndexError
    if link_chemistry <= 1.6:
        if position_chemistry == 0:
            return 2
        if position_chemistry == 1:
            return 5
        if position_chemistry == 2:
            return 8
        if position_chemistry == 3:
            return 9
        raise IndexError
    if link_chemistry > 1.6:
        if position_chemistry == 0:
            return 2
        if position_chemistry == 1:
            return 5
        if position_chemistry == 2:
            return 9
        if position_chemistry == 3:
            return 10
        raise IndexError
    raise IndexError

    
class Formation:
    
    def __init__(self, slots, links):
        """
        Creates instance of Formation.
        Args:
            slots: list of Slot instances.
            links: list of Link instances.
        Returns:
            instance of Formation.
        """
        self.slots = slots
        self.links = links
        
    def get_chemistry(self):
        """Calculates chemistry of formation. Makes sure it is less of equal to 100."""
        return np.min([np.sum([s.get_chemistry() for s in self.slots.values()]), 100])
    
    def get_rating(self):
        """Calculates rating of formation."""
        return np.sum([s.player.data.overall for s in self.slots.values()]) / 11.
    
    def get_price(self):
        """Calculates price of formation."""
        return np.sum([s.player.data.price_ps4 for s in self.slots.values()])
        
    def __repr__(self):
        return "{}(slots={}, links={})".format(self.__class__.__name__, self.slots, self.links)
    
