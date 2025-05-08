from minisom import MiniSom
import numpy as np

# Datos de ejemplo
data = np.random.rand(100, 3)  # Datos aleatorios

# Inicializamos el mapa autoorganizado de Kohonen
som = MiniSom(5, 5, 3, sigma=0.3, learning_rate=0.5)  # 5x5 mapa con 3 características
som.train_random(data, 100)  # Entrenamos el mapa

# Mostrar pesos
print("Pesos de la SOM:", som.get_weights())  # Imprimimos los pesos

# Ejemplo de aplicación real: En el análisis de datos, los mapas autoorganizados de Kohonen pueden ser utilizados para visualizar y agrupar datos en un espacio de menor dimensión, considerando la topología del mapa.
