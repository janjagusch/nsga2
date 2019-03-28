class Stopper:
    """
    This class stops the genetic optimization process, provided a genetic state.
    """

    def stop(self, population):
        """
        Stops the genetic optimization, if the state satisfies a certain
        condition.
        Args:
            state: a genetic optimization state.
        Returns:
            a booolean, indicating whether the search should be stopped.
        """
        return True


class MaxGenerationStopper(Stopper):
    """
    This class stops the genetic optimization process after a defined number
    of generations.
    """

    def __init__(self, max_generation=100):
        self.max_generation = max_generation
        self.current_generation = 0

    def stop(self, population):
        if self.current_generation >= self.max_generation:
            return True
        self.current_generation += 1
        return False
