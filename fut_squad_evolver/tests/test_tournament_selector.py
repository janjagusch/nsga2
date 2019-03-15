from ..nsga2.tournament_selector import TournamentSelector


def test_select():
    selector = TournamentSelector(10)

    individual_a = {"fitness": {"rank": 0, "crowding_distance": 0.5}}
    individual_b = {"fitness": {"rank": 1, "crowding_distance": 1}}
    assert selector._select(individual_a, individual_b) == individual_a

    individual_a = {"fitness": {"rank": 1, "crowding_distance": 0.5}}
    individual_b = {"fitness": {"rank": 0, "crowding_distance": 1}}
    assert selector._select(individual_a, individual_b) == individual_b

    individual_a = {"fitness": {"rank": 1, "crowding_distance": 1}}
    individual_b = {"fitness": {"rank": 1, "crowding_distance": 0.5}}
    assert selector._select(individual_a, individual_b) == individual_a

    individual_a = {"fitness": {"rank": 1, "crowding_distance": 0.5}}
    individual_b = {"fitness": {"rank": 1, "crowding_distance": 1}}
    assert selector._select(individual_a, individual_b) == individual_b

    individual_a = {"fitness": {"rank": 1, "crowding_distance": 1}}
    individual_b = {"fitness": {"rank": 1, "crowding_distance": 1}}
    assert selector._select(individual_a, individual_b) in (individual_a, individual_b)


def test_populate():
    population_size = 10
    selector = TournamentSelector(population_size)

    individual_a = {"fitness": {"rank": 0, "crowding_distance": 0.5}}
    individual_b = {"fitness": {"rank": 1, "crowding_distance": 1}}
    population = [individual_a, individual_b]

    new_population = selector.populate(population)
    assert len(new_population) == population_size
