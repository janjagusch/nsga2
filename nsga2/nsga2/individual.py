"""
This module describes an individual in the genetic pool.
"""
INDIVIDUAL_COUNTER = 0


def get_individual_id():
    global INDIVIDUAL_COUNTER
    counter = INDIVIDUAL_COUNTER
    INDIVIDUAL_COUNTER += 1
    return counter


class Individual:

    def __init__(self, genotype, phenotype=None, fitness=None, individual_id=None):
        if individual_id is None:
            individual_id = get_individual_id()
        self.individual_id = individual_id
        self.genotype = genotype
        if phenotype is None:
            phenotype = {}
        self.phenotype = phenotype
        if fitness is None:
            fitness = {}
        self.fitness = fitness

    def evaluate(self):
        self.phenotype = self.genotype.evaluate()

    def __repr__(self):
        repr = "{}(individual_id={}, phenotype={}, fitness={})".\
            format(self.__class__.__name__, self.individual_id, self.phenotype, self.fitness)
        return repr
