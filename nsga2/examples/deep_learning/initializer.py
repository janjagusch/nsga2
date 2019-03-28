import numpy as np

from nsga2.examples.deep_learning.genotype import NeuralNetwork
from nsga2.nsga2.initializer import Initializer


class NNInitializer(Initializer):

    def __init__(self, n_individuals,
                 data, target, is_classification, solver="lbfgs",
                 n_layer_range=(1, 10), n_nodes_range=(2, 100), activations=None):
        super().__init__(n_individuals)
        self.data = data
        self.target = target
        self.is_classification = is_classification
        self.solver = solver
        self.n_layer_range = n_layer_range
        self.n_nodes_range = n_nodes_range
        if activations is None:
            activations = ["identity", "logistic", "tanh", "relu"]
        self.activations = activations

    def _initialize_genotype(self):
        n_layers = np.random.randint(*self.n_layer_range)
        n_nodes = np.random.randint(*self.n_nodes_range)
        activation = np.random.choice(self.activations)
        return NeuralNetwork(n_layers=n_layers, n_nodes=n_nodes,
                             activation=activation, data=self.data,
                             target=self.target,
                             is_classification=self.is_classification,
                             solver=self.solver)
