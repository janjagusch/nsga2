class NSGA2:

    def __init__(self, initializer, evaluator, selector, crossover, mutator, stopper):
        self.initializer = initializer
        self.evaluator = evaluator
        self.selector = selector
        self.crossover = crossover
        self.mutator = mutator
        self.stopper = stopper
        self.population = None
        self.population_log = []

    def make_phenotype(self, population):
        for individual in population.values():
            individual.evaluate()

    def make_next_population(self, champions):
        next_population = {}
        for parent_a, parent_b in zip(champions[::2], champions[1::2]):
            child_a, child_b = self.crossover.crossover(parent_a, parent_b)
            next_population[child_a.individual_id] = child_a
            next_population[child_b.individual_id] = child_b
        for individual in next_population.values():
            self.mutator.mutate(individual)
        return next_population

    def search(self, verbose=False):
        if verbose:
            print("Initialize population...")
        population = self.initializer.initialize()
        self.make_phenotype(population)
        self.evaluator.evaluate(population)
        self.population_log.append(population)
        if verbose:
            print("Run search...")
        interrupt = False
        while not self.stopper.stop(population):
            try:
                champions = self.selector.select(population)
                next_population = self.make_next_population(champions)
                self.make_phenotype(next_population)
                self.evaluator.evaluate(next_population)
                population = next_population
                self.population_log.append(population)
            except KeyboardInterrupt:
                if verbose:
                    print("Search interrupted...")
                break
        if verbose:
            print("Terminating search...")
        self.population = population
        return population
