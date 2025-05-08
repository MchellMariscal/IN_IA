import numpy as np
import matplotlib.pyplot as plt

# Simular posiciones de un objeto moviéndose
tiempo = np.linspace(0, 10, 100)  # Generamos 100 puntos de tiempo entre 0 y 10
posicion = 5 * tiempo  # Movimiento rectilíneo uniforme

plt.plot(tiempo, posicion)  # Graficamos la posición en función del tiempo
plt.xlabel('Tiempo')  # Etiqueta del eje x
plt.ylabel('Posición')  # Etiqueta del eje y
plt.title('Movimiento Uniforme')  # Título del gráfico
plt.grid(True)  # Mostramos la cuadrícula
plt.show()  # Mostramos el gráfico

# Ejemplo de aplicación real: En la robótica, el movimiento puede ser utilizado para modelar la trayectoria de un robot, considerando la posición en función del tiempo para planificar rutas y acciones.

