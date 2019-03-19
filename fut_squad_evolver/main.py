from fut_squad_evolver.nsga2.initializer import make_initializer
from fut_squad_evolver.utils.read_write import read_file

players = read_file("data/processed", "ut_players.p")

initializer = make_initializer("CompatibilityInitializer", {"formation_id": "442", "min_compatibility": 2})

squad = initializer.initialize(players)

squad.evaluate("442")
