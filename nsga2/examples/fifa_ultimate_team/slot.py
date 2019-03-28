class Slot:

    def __init__(self, player, is_locked):
        self.player = player
        self.is_locked = is_locked

    def __repr__(self):
        repr = "{}(player={}, is_locked={})".format(self.__class__.__name__, self.player, self.is_locked)
        return repr
