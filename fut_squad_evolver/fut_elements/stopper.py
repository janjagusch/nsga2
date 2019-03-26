from fut_squad_evolver.nsga2.stopper import Stopper


class SquadStopper(Stopper):

    def __init__(self, max_price=None, min_overall=None, min_chemistry=None, min_matches=1):
        self.max_price = max_price
        self.min_overall = min_overall
        self.min_chemistry = min_chemistry
        self.min_matches = min_matches

    def stop(self, population):
        individuals_matched = [individual for individual in population.values() if
                               (individual.phenotype["price"] <= self.max_price or self.max_price is None) and
                               (individual.phenotype["overall"] >= self.min_overall or self.min_overall is None) and
                               (individual.phenotype["chemistry"] >= self.min_chemistry or self.min_chemistry is None)]
        if len(individuals_matched) >= self.min_matches:
            return True
        return False
