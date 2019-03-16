class Stopper:
    """
    This class stops the genetic optimization process, provided a genetic state.
    """

    def stop(self, state):
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

    def __init__(self, max_generations=100):
        self.max_generations = max_generations

    def stop(self, state):
        if state["current_generation"] >= self.max_generations:
            return True
        return False


STOPPER_MAP = {
    "MaxGenerationStopper": MaxGenerationStopper
}


def make_stopper(stopper_id, stopper_kwargs=None):
    if stopper_kwargs is None:
        stopper_kwargs = {}
    if stopper_id not in STOPPER_MAP.keys():
        raise ValueError
    return STOPPER_MAP[stopper_id](**stopper_kwargs)
