import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf

# Parámetros
n = 500  # número de muestras
mu = 0   # media
sigma = 1  # desviación estándar

# Generar proceso estacionario (ruido blanco)
np.random.seed(0)
white_noise = np.random.normal(mu, sigma, n)

# Calcular propiedades
media = np.mean(white_noise)
varianza = np.var(white_noise)

print(f"Media: {media:.4f}")
print(f"Varianza: {varianza:.4f}")

# Graficar proceso
plt.figure(figsize=(10, 4))
plt.plot(white_noise, label="Ruido Blanco")
plt.title("Proceso Estacionario: Ruido Blanco")
plt.xlabel("Tiempo")
plt.ylabel("Valor")
plt.grid(True)
plt.legend()
plt.show()

# Graficar autocorrelación
plot_acf(white_noise, lags=40)
plt.title("Autocorrelación del Ruido Blanco")
plt.show()
