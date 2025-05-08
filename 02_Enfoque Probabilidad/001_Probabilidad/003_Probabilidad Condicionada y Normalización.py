# Probabilidades no normalizadas (posteriores antes de aplicar P(E))
posteriores = {
    "hipotesis_1": 0.6,  # Probabilidad de la hipótesis 1
    "hipotesis_2": 0.3,  # Probabilidad de la hipótesis 2
    "hipotesis_3": 0.1   # Probabilidad de la hipótesis 3
}

# Normalización de las probabilidades
total = sum(posteriores.values())  # Suma de las probabilidades
normalizadas = {k: v / total for k, v in posteriores.items()}  # Normalizamos las probabilidades

print("Probabilidades normalizadas:")  # Imprimimos las probabilidades normalizadas
for h, p in normalizadas.items():  # Para cada hipótesis
    print(f"{h}: {p:.2f}")  # Imprimimos la hipótesis y su probabilidad normalizada

# Ejemplo de aplicación real: En el análisis de datos, la normalización de probabilidades puede ser utilizada para ajustar las probabilidades condicionales, asegurando que sumen 1 y sean comparables.
