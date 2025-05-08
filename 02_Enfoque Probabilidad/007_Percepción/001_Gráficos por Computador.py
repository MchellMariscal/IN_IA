import matplotlib.pyplot as plt
import numpy as np

# Dibujar un círculo
theta = np.linspace(0, 2*np.pi, 100)  # Generamos 100 puntos entre 0 y 2π
x = np.cos(theta)  # Coordenadas x del círculo
y = np.sin(theta)  # Coordenadas y del círculo

plt.plot(x, y)  # Graficamos el círculo
plt.title('Círculo en 2D')  # Título del gráfico
plt.axis('equal')  # Aseguramos que los ejes tengan la misma escala
plt.show()  # Mostramos el gráfico

# Ejemplo de aplicación real: En el diseño gráfico, los gráficos por computador pueden ser utilizados para crear y visualizar formas geométricas, como círculos, en aplicaciones de diseño y modelado.
