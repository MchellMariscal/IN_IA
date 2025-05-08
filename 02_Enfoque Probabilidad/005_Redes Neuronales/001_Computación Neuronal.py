import numpy as np

# Función para calcular la salida de una neurona artificial simple
def neuron_output(inputs, weights, bias):
    """Calcula la salida de una neurona artificial simple"""
    total_input = np.dot(inputs, weights) + bias  # Calculamos la entrada total como la suma ponderada de las entradas más el sesgo
    output = activation_function(total_input)  # Aplicamos la función de activación
    return output  # Devolvemos la salida

# Función de activación escalón
def activation_function(x):
    """Función de activación escalón"""
    return 1 if x >= 0 else 0  # Devolvemos 1 si la entrada es mayor o igual a 0, 0 en caso contrario

# Definimos entradas, pesos y sesgo
inputs = np.array([1, 0])      # Entradas de la neurona
weights = np.array([0.6, -0.4]) # Pesos sinápticos
bias = 0.2                      # Sesgo

# Cálculo de la salida de la neurona
output = neuron_output(inputs, weights, bias)  # Calculamos la salida de la neurona

print("Entradas:", inputs)  # Imprimimos las entradas
print("Pesos:", weights)  # Imprimimos los pesos
print("Sesgo:", bias)  # Imprimimos el sesgo
print("Salida de la neurona:", output)  # Imprimimos la salida de la neurona

# Ejemplo de aplicación real: En el procesamiento de señales, la computación neuronal puede ser utilizada para modelar la respuesta de una neurona a diferentes entradas, considerando los pesos y el sesgo.
