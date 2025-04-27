import numpy as np
from hmmlearn import hmm

# Modelo HMM
model = hmm.MultinomialHMM(n_components=2, random_state=42)
model.startprob_ = np.array([0.6, 0.4])
model.transmat_ = np.array([[0.7, 0.3], [0.4, 0.6]])
model.emissionprob_ = np.array([[0.9, 0.1], [0.2, 0.8]])

# Observaciones: 0 = no paraguas, 1 = paraguas
observaciones = np.array([[1], [1], [0], [1], [0]])

logprob, estados = model.decode(observaciones, algorithm="viterbi")
print("Secuencia de estados más probable:", estados)
