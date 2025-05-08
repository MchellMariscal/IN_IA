import numpy as np

# Clase para la red de Hopfield
class HopfieldNetwork:
    def __init__(self, n_neurons):
        self.weights = np.zeros((n_neurons, n_neurons))  # Inicializamos los pesos

    def train(self, patterns):
        for p in patterns:  # Para cada patrón
            self.weights += np.outer(p, p)  # Actualizamos los pesos
        np.fill_diagonal(self.weights, 0)  # Eliminamos la diagonal

    def recall(self, pattern, steps=5):
        for _ in range(steps):  # Para cada paso
            pattern = np.sign(self.weights @ pattern)  # Actualizamos el patrón
        return pattern  # Devolvemos el patrón recordado

# Patrones de ejemplo
patterns = np.array([[1, -1, 1, -1], [-1, 1, -1, 1]])  # Patrones de entrenamiento
hopfield = HopfieldNetwork(4)  # Inicializamos la red de Hopfield
hopfield.train(patterns)  # Entrenamos la red

# Recuperación de un patrón
pattern = np.array([1, -1, -1, -1])  # Patrón de entrada
recalled = hopfield.recall(pattern)  # Recordamos el patrón
print("Patrón recordado:", recalled)  # Imprimimos el patrón recordado

# Ejemplo de aplicación real: En el almacenamiento y recuperación de patrones, las redes de Hopfield pueden ser utilizadas para recordar patrones completos a partir de versiones parciales o ruidosas, considerando la actualización de los pesos.
