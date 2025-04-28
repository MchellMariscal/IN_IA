import numpy as np

# Hopfield
class HopfieldNetwork:
    def __init__(self, n_neurons):
        self.weights = np.zeros((n_neurons, n_neurons))

    def train(self, patterns):
        for p in patterns:
            self.weights += np.outer(p, p)
        np.fill_diagonal(self.weights, 0)

    def recall(self, pattern, steps=5):
        for _ in range(steps):
            pattern = np.sign(self.weights @ pattern)
        return pattern

# Patrones
patterns = np.array([[1, -1, 1, -1], [-1, 1, -1, 1]])
hopfield = HopfieldNetwork(4)
hopfield.train(patterns)

# Recuperación
pattern = np.array([1, -1, -1, -1])
recalled = hopfield.recall(pattern)
print("Patrón recordado:", recalled)
