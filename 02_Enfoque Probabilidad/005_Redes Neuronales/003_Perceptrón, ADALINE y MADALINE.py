import numpy as np

# Perceptrón
class Perceptron:
    def __init__(self, lr=0.1, epochs=10):
        self.lr = lr
        self.epochs = epochs

    def fit(self, X, y):
        self.weights = np.zeros(X.shape[1])
        self.bias = 0
        for _ in range(self.epochs):
            for xi, target in zip(X, y):
                update = self.lr * (target - self.predict(xi))
                self.weights += update * xi
                self.bias += update

    def predict(self, X):
        return np.where(np.dot(X, self.weights) + self.bias >= 0, 1, 0)

# ADALINE
class Adaline:
    def __init__(self, lr=0.01, epochs=10):
        self.lr = lr
        self.epochs = epochs

    def fit(self, X, y):
        self.weights = np.zeros(X.shape[1])
        self.bias = 0
        for _ in range(self.epochs):
            output = self.activation(X)
            errors = y - output
            self.weights += self.lr * X.T.dot(errors)
            self.bias += self.lr * errors.sum()

    def activation(self, X):
        return np.dot(X, self.weights) + self.bias

    def predict(self, X):
        return np.where(self.activation(X) >= 0, 1, 0)

# Datos simples
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([0, 0, 0, 1])  # AND lógico

# Probar Perceptrón
p = Perceptron()
p.fit(X, y)
print("Predicciones Perceptrón:", p.predict(X))

# Probar Adaline
a = Adaline()
a.fit(X, y)
print("Predicciones Adaline:", a.predict(X))
