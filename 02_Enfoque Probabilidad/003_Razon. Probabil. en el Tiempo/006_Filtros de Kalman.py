import numpy as np

# Parámetros
pos = 0.0  # Posición inicial
vel = 1.0  # Velocidad
medida_ruido = 2.0  # Ruido de la medida
proceso_ruido = 0.5  # Ruido del proceso
medida_real = [1, 2, 3, 4, 6, 7]  # Simulación de sensores

# Estado inicial
estado_estimado = 0.0  # Estado estimado inicial
incertidumbre = 1.0  # Incertidumbre inicial

print("Simulación de Filtro de Kalman:")  # Imprimimos el título
for medida in medida_real:  # Para cada medida
    # Predicción
    estado_estimado = estado_estimado + vel  # Actualizamos el estado estimado
    incertidumbre = incertidumbre + proceso_ruido  # Actualizamos la incertidumbre

    # Corrección
    ganancia = incertidumbre / (incertidumbre + medida_ruido)  # Calculamos la ganancia
    estado_estimado = estado_estimado + ganancia * (medida - estado_estimado)  # Actualizamos el estado estimado
    incertidumbre = (1 - ganancia) * incertidumbre  # Actualizamos la incertidumbre

    print(f"Medida: {medida:.2f}, Estado estimado: {estado_estimado:.2f}")  # Imprimimos la medida y el estado estimado

# Ejemplo de aplicación real: En la navegación, los filtros de Kalman pueden ser utilizados para estimar la posición y velocidad de un objeto en movimiento, considerando las mediciones ruidosas y las incertidumbres del proceso.
