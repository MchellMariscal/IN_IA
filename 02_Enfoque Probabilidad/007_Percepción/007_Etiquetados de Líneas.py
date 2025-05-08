import cv2
import numpy as np
import matplotlib.pyplot as plt

# Crear una imagen con líneas
imagen = np.zeros((100, 100), dtype=np.uint8)  # Creamos una imagen negra
cv2.line(imagen, (10, 10), (90, 10), 255, 2)  # Dibujamos una línea horizontal
cv2.line(imagen, (10, 20), (90, 20), 255, 2)  # Dibujamos otra línea horizontal

# Detección de líneas con Hough
bordes = cv2.Canny(imagen, 50, 150)  # Detectamos los bordes
lineas = cv2.HoughLinesP(bordes, 1, np.pi/180, threshold=20, minLineLength=10, maxLineGap=5)  # Detectamos las líneas

# Dibujar líneas detectadas
imagen_color = cv2.cvtColor(imagen, cv2.COLOR_GRAY2BGR)  # Convertimos la imagen a color
for linea in lineas:  # Para cada línea detectada
    x1, y1, x2, y2 = linea[0]  # Coordenadas de la línea
    cv2.line(imagen_color, (x1, y1), (x2, y2), (0, 255, 0), 2)  # Dibujamos la línea en verde

plt.imshow(imagen_color)  # Mostramos la imagen con las líneas detectadas
plt.title('Líneas Detectadas')  # Título del gráfico
plt.show()  # Mostramos el gráfico

# Ejemplo de aplicación real: En la visión por computador, el etiquetado de líneas puede ser utilizado para identificar y etiquetar líneas en imágenes, facilitando el análisis de estructuras y patrones.
