import numpy as np
import matplotlib.pyplot as plt

# Definimos varias funciones de activación
def step_function(x):
    return np.where(x >= 0, 1, 0)  # Función escalón

def sigmoid(x):
    return 1 / (1 + np.exp(-x))  # Función sigmoide

def tanh(x):
    return np.tanh(x)  # Función tangente hiperbólica

def relu(x):
    return np.maximum(0, x)  # Función ReLU

# Valores para graficar
x = np.linspace(-10, 10, 100)  # Valores de x para graficar

# Graficar todas las funciones de activación
plt.figure(figsize=(10, 7))  # Tamaño de la figura

plt.subplot(2, 2, 1)  # Subgráfico 1
plt.plot(x, step_function(x))  # Graficamos la función escalón
plt.title('Step Function')  # Título del subgráfico

plt.subplot(2, 2, 2)  # Subgráfico 2
plt.plot(x, sigmoid(x))  # Graficamos la función sigmoide
plt.title('Sigmoid')  # Título del subgráfico

plt.subplot(2, 2, 3)  # Subgráfico 3
plt.plot(x, tanh(x))  # Graficamos la función tangente hiperbólica
plt.title('Tanh')  # Título del subgráfico

plt.subplot(2, 2, 4)  # Subgráfico 4
plt.plot(x, relu(x))  # Graficamos la función ReLU
plt.title('ReLU')  # Título del subgráfico

plt.tight_layout()  # Ajustamos el diseño
plt.show()  # Mostramos el gráfico

# Ejemplo de aplicación real: En el diseño de redes neuronales, las funciones de activación pueden ser utilizadas para introducir no linealidades en el modelo, permitiendo la aproximación de funciones complejas.
