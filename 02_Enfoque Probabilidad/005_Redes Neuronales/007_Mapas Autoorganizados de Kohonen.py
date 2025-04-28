from minisom import MiniSom
import numpy as np

# Datos
data = np.random.rand(100, 3)

# SOM
som = MiniSom(5, 5, 3, sigma=0.3, learning_rate=0.5)
som.train_random(data, 100)

# Mostrar pesos
print("Pesos de la SOM:", som.get_weights())
