import cv2
import numpy as np
import matplotlib.pyplot as plt

# Imagen: imagen negra con un rectángulo blanco
imagen = np.zeros((100, 100), dtype=np.uint8)  # Creamos una imagen negra
imagen[30:70, 30:70] = 255  # Dibujamos un rectángulo blanco

# Detectar bordes usando el algoritmo de Canny
bordes = cv2.Canny(imagen, 50, 150)  # Aplicamos la detección de bordes

plt.imshow(bordes, cmap='gray')  # Mostramos los bordes detectados
plt.title('Detección de Bordes (Canny)')  # Título del gráfico
plt.show()  # Mostramos el gráfico

# Ejemplo de aplicación real: En la visión por computador, la detección de aristas puede ser utilizada para identificar los bordes de objetos en imágenes, facilitando la segmentación y el análisis de escenas.
