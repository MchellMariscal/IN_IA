import numpy as np
import matplotlib.pyplot as plt

# Simular posiciones de un objeto moviéndose
tiempo = np.linspace(0, 10, 100)
posicion = 5 * tiempo  # movimiento rectilíneo uniforme

plt.plot(tiempo, posicion)
plt.xlabel('Tiempo')
plt.ylabel('Posición')
plt.title('Movimiento Uniforme')
plt.grid(True)
plt.show()
