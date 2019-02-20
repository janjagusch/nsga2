from formation_base import Formation, get_position, make_links, Slot, Link


_FORMATION_MAP = {}


def make_formation(slots, links):
    """Creates formation from slots dictionary and links list."""
    slots = {k: Slot(k, get_position(v)) for k, v in slots.items()}
    links = make_links(links, slots)
    return Formation(slots, links)
    

# Creating 433 formation.
# Creating slots.
slots = {
    "GK": "GK",
    "LB": "LB",
    "CB1": "CB",
    "CB2": "CB",
    "RB": "RB",
    "CM1": "CM",
    "CM2": "CM",
    "CM3": "CM",
    "LW": "LW",
    "ST": "ST",
    "RW": "RW"
}
# Creating links.
links = [("GK", "CB1"), ("GK", "CB2"),
         ("LB", "CB1"), ("CB1", "CB2"), ("CB2", "RB"), 
         ("LB", "CM1"), ("CB1", "CM2"), ("CB2", "CM2"), ("RB", "CM3"),
         ("CM1", "CM2"), ("CM2", "CM3"),
         ("CM1", "LW"), ("CM2", "ST"), ("CM3", "RW"),
         ("LW", "ST"), ("ST", "RW")
        ]
# Adding to formation map.
_FORMATION_MAP["433"] = make_formation(slots, links)


# Creating 5221 formation.
# Creating slots.
slots = {
    "GK": "GK",
    "LWB": "LWB",
    "CB1": "CB",
    "CB2": "CB",
    "CB3": "CB",
    "RWB": "RWB",
    "CM1": "CM",
    "CM2": "CM",
    "LW": "LW",
    "ST": "ST",
    "RW": "RW"
}
# Creating links.
links = [("GK", "CB1"), ("GK", "CB2"), ("GK", "CB3"),
         ("LWB", "CB1"), ("CB1", "CB2"), ("CB2", "CB3"), ("CB3", "RWB"),
         ("LWB", "LW"), ("LWB", "CM1"), ("CB2", "CM1"), ("CB2", "CM2"), ("RWB", "RW"), ("RWB", "CM2"),
         ("CM1", "CM2"),
         ("CM1", "LW"), ("CM1", "ST"), ("CM2", "ST"), ("CM2", "RW"),
         ("LW", "ST"), ("ST", "RW")
        ]
# Adding to formation map.
_FORMATION_MAP["5221"] = make_formation(slots, links)


def get_formation(formation):
    return _FORMATION_MAP[formation]
