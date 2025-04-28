import numpy as np

# Simulación de una neurona simple
def neuron_output(inputs, weights, bias):
    """Calcula la salida de una neurona artificial simple"""
    total_input = np.dot(inputs, weights) + bias
    output = activation_function(total_input)
    return output

def activation_function(x):
    """Función de activación escalón"""
    return 1 if x >= 0 else 0

# Definimos entradas, pesos y sesgo
inputs = np.array([1, 0])      # Entradas de la neurona
weights = np.array([0.6, -0.4]) # Pesos sinápticos
bias = 0.2                      # Sesgo

# Cálculo
output = neuron_output(inputs, weights, bias)

print("Entradas:", inputs)
print("Pesos:", weights)
print("Sesgo:", bias)
print("Salida de la neurona:", output)
