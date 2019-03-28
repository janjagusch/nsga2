"""
This class describes the Genotype, which needs to specified for every new
project.
"""

class Genotype:
    """
    An abstract class that you need to inherit from to create your own
    problem specific genotype.
    """

    def evaluate(self):
        """
        This method evaluates the performance of the genotype and returns a
        dictionary of objectives, such as for example:
        {"objective_a": 1, "objective_b": 2}.
        """
        return {}
