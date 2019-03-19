"""
Describes a squad formation, such as a 442 formation.
"""


class Formation:

    def __init__(self, positions, links, labels, locations=None):
        self.positions = positions
        self.links = links
        self.labels = labels
        if locations is None:
            locations = {}
        self.locations = locations
