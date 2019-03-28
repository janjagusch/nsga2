import pickle
import sys

import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.neural_network import MLPClassifier, MLPRegressor

from nsga2.nsga2.genotype import Genotype


class NeuralNetwork(Genotype):

    def __init__(self, n_layers, n_nodes,
                 activation, data, target,
                 is_classification=True, solver="lbfgs"):
        self.n_layers = n_layers
        self.n_nodes = n_nodes
        self.activation = activation
        self.solver = solver
        self.is_classification = is_classification
        hidden_layer_sizes = [self.n_nodes for _ in range(self.n_layers)]
        if is_classification:
            self.model = MLPClassifier(hidden_layer_sizes=hidden_layer_sizes,
                                       activation=self.activation,
                                       solver=self.solver)
        else:
            self.model = MLPRegressor(hidden_layer_sizes=hidden_layer_sizes,
                                      activation=self.activation,
                                      solver=self.solver)
        self.data = data
        self.target = target

    def evaluate(self):
        self.model.fit(self.data, self.target)
        size = sys.getsizeof(pickle.dumps(self.model)) / 1048576
        score = np.mean(cross_val_score(self.model, self.data, self.target, cv=5))
        return {
            "size": size,
            "score": score
        }
