import numpy as np
from hmmlearn import hmm

# Modelo HMM
model = hmm.MultinomialHMM(n_components=2, random_state=42)  # Inicializamos el modelo
model.startprob_ = np.array([0.6, 0.4])  # Probabilidades iniciales
model.transmat_ = np.array([[0.7, 0.3], [0.4, 0.6]])  # Matriz de transición
model.emissionprob_ = np.array([[0.9, 0.1], [0.2, 0.8]])  # Probabilidades de emisión

# Observaciones: 0 = no paraguas, 1 = paraguas
observaciones = np.array([[1], [1], [0], [1], [0]])

# Decodificar la secuencia de estados más probable
logprob, estados = model.decode(observaciones, algorithm="viterbi")  # Decodificamos la secuencia
print("Secuencia de estados más probable:", estados)  # Imprimimos la secuencia de estados

# Ejemplo de aplicación real: En el análisis de series temporales, los modelos de Markov ocultos pueden ser utilizados para identificar patrones en datos secuenciales, considerando las transiciones entre estados ocultos y las observaciones.
