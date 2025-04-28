import numpy as np
import matplotlib.pyplot as plt

# Definimos varias funciones de activación
def step_function(x):
    return np.where(x >= 0, 1, 0)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def tanh(x):
    return np.tanh(x)

def relu(x):
    return np.maximum(0, x)

# Valores para graficar
x = np.linspace(-10, 10, 100)

# Graficar todas
plt.figure(figsize=(10, 7))

plt.subplot(2, 2, 1)
plt.plot(x, step_function(x))
plt.title('Step Function')

plt.subplot(2, 2, 2)
plt.plot(x, sigmoid(x))
plt.title('Sigmoid')

plt.subplot(2, 2, 3)
plt.plot(x, tanh(x))
plt.title('Tanh')

plt.subplot(2, 2, 4)
plt.plot(x, relu(x))
plt.title('ReLU')

plt.tight_layout()
plt.show()
