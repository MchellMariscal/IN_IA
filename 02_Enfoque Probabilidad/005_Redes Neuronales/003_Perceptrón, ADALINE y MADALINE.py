import numpy as np

# Clase para el Perceptrón
class Perceptron:
    def __init__(self, lr=0.1, epochs=10):
        self.lr = lr  # Tasa de aprendizaje
        self.epochs = epochs  # Número de épocas

    def fit(self, X, y):
        self.weights = np.zeros(X.shape[1])  # Inicializamos los pesos
        self.bias = 0  # Inicializamos el sesgo
        for _ in range(self.epochs):  # Para cada época
            for xi, target in zip(X, y):  # Para cada ejemplo de entrenamiento
                update = self.lr * (target - self.predict(xi))  # Calculamos la actualización
                self.weights += update * xi  # Actualizamos los pesos
                self.bias += update  # Actualizamos el sesgo

    def predict(self, X):
        return np.where(np.dot(X, self.weights) + self.bias >= 0, 1, 0)  # Predecimos la salida

# Clase para ADALINE
class Adaline:
    def __init__(self, lr=0.01, epochs=10):
        self.lr = lr  # Tasa de aprendizaje
        self.epochs = epochs  # Número de épocas

    def fit(self, X, y):
        self.weights = np.zeros(X.shape[1])  # Inicializamos los pesos
        self.bias = 0  # Inicializamos el sesgo
        for _ in range(self.epochs):  # Para cada época
            output = self.activation(X)  # Calculamos la salida
            errors = y - output  # Calculamos los errores
            self.weights += self.lr * X.T.dot(errors)  # Actualizamos los pesos
            self.bias += self.lr * errors.sum()  # Actualizamos el sesgo

    def activation(self, X):
        return np.dot(X, self.weights) + self.bias  # Calculamos la activación

    def predict(self, X):
        return np.where(self.activation(X) >= 0, 1, 0)  # Predecimos la salida

# Datos simples para el problema AND
X = np.array([[0,0],[0,1],[1,0],[1,1]])  # Entradas
y = np.array([0, 0, 0, 1])  # Salidas

# Probar Perceptrón
p = Perceptron()  # Inicializamos el perceptrón
p.fit(X, y)  # Ajustamos el perceptrón
print("Predicciones Perceptrón:", p.predict(X))  # Imprimimos las predicciones

# Probar ADALINE
a = Adaline()  # Inicializamos ADALINE
a.fit(X, y)  # Ajustamos ADALINE
print("Predicciones Adaline:", a.predict(X))  # Imprimimos las predicciones

# Ejemplo de aplicación real: En la clasificación binaria, el perceptrón y ADALINE pueden ser utilizados para aprender patrones en datos, considerando las actualizaciones de pesos y sesgo para mejorar las predicciones.
