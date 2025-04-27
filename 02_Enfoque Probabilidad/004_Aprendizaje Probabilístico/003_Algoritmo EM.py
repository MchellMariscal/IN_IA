import numpy as np

# Datos simulados
datos = np.hstack((np.random.normal(0, 1, 50), np.random.normal(5, 1, 50)))

# Inicialización
media1, media2 = 0, 5

for i in range(5):
    # E-step
    prob1 = np.exp(-(datos - media1)**2)
    prob2 = np.exp(-(datos - media2)**2)
    w1 = prob1 / (prob1 + prob2)

    # M-step
    media1 = np.sum(w1 * datos) / np.sum(w1)
    media2 = np.sum((1 - w1) * datos) / np.sum(1 - w1)

print(f"Media final 1: {media1:.2f}, Media final 2: {media2:.2f}")
