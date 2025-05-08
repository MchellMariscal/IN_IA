import numpy as np

# Datos simulados: mezcla de dos distribuciones normales
datos = np.hstack((np.random.normal(0, 1, 50), np.random.normal(5, 1, 50)))

# Inicialización de las medias
media1, media2 = 0, 5

for i in range(5):  # Iteraciones del algoritmo EM
    # Paso E: calcular las probabilidades de pertenencia a cada distribución
    prob1 = np.exp(-(datos - media1)**2)  # Probabilidad para la primera distribución
    prob2 = np.exp(-(datos - media2)**2)  # Probabilidad para la segunda distribución
    w1 = prob1 / (prob1 + prob2)  # Peso para la primera distribución

    # Paso M: actualizar las medias
    media1 = np.sum(w1 * datos) / np.sum(w1)  # Actualizamos la media de la primera distribución
    media2 = np.sum((1 - w1) * datos) / np.sum(1 - w1)  # Actualizamos la media de la segunda distribución

print(f"Media final 1: {media1:.2f}, Media final 2: {media2:.2f}")  # Imprimimos las medias finales

# Ejemplo de aplicación real: En el análisis de datos, el algoritmo EM puede ser utilizado para identificar grupos en datos sin etiquetar, considerando las distribuciones subyacentes y ajustando los parámetros para maximizar la verosimilitud.
