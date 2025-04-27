import numpy as np

# Parámetros
pos = 0.0
vel = 1.0
medida_ruido = 2.0
proceso_ruido = 0.5
medida_real = [1, 2, 3, 4, 6, 7]  # Simulación de sensores

# Estado inicial
estado_estimado = 0.0
incertidumbre = 1.0

print("Simulación de Filtro de Kalman:")
for medida in medida_real:
    # Predicción
    estado_estimado = estado_estimado + vel
    incertidumbre = incertidumbre + proceso_ruido

    # Corrección
    ganancia = incertidumbre / (incertidumbre + medida_ruido)
    estado_estimado = estado_estimado + ganancia * (medida - estado_estimado)
    incertidumbre = (1 - ganancia) * incertidumbre

    print(f"Medida: {medida:.2f}, Estado estimado: {estado_estimado:.2f}")
