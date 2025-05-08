import random

# Definimos las distribuciones condicionales para una red bayesiana simple
# P(R) - Probabilidad de que llueva
P_R = {
    True: 0.2,  # Probabilidad de que llueva
    False: 0.8   # Probabilidad de que no llueva
}

# P(S | R) - Probabilidad de que el suelo esté mojado dado que llueve o no
P_S_given_R = {
    True: {True: 0.9, False: 0.1},  # P(S=True | R=True), P(S=False | R=True)
    False: {True: 0.2, False: 0.8}  # P(S=True | R=False), P(S=False | R=False)
}

# Muestreo Directo: genera muestras de R y S directamente desde la red

def muestreo_directo(n):
    muestras = []  # Lista para guardar las muestras
    for _ in range(n):  # Para cada muestra
        r = random.choices([True, False], weights=[P_R[True], P_R[False]])[0]  # Muestreo de R
        s = random.choices([True, False], weights=[P_S_given_R[r][True], P_S_given_R[r][False]])[0]  # Muestreo de S dado R
        muestras.append((r, s))  # Guardamos la muestra
    return muestras  # Devolvemos las muestras

# Muestreo por Rechazo: sólo acepta muestras que coincidan con la evidencia S=True

def muestreo_por_rechazo(n):
    aceptadas = []  # Lista para guardar las muestras aceptadas
    total = 0  # Contador de intentos totales
    while len(aceptadas) < n:  # Mientras no tengamos suficientes muestras aceptadas
        r = random.choices([True, False], weights=[P_R[True], P_R[False]])[0]  # Muestreo de R
        s = random.choices([True, False], weights=[P_S_given_R[r][True], P_S_given_R[r][False]])[0]  # Muestreo de S dado R
        total += 1  # Incrementamos el contador de intentos
        if s is True:  # Si la muestra coincide con la evidencia
            aceptadas.append(r)  # Guardamos la muestra aceptada
    prob_lluvia_dado_s = aceptadas.count(True) / len(aceptadas)  # Probabilidad de R=True dado S=True
    return prob_lluvia_dado_s, total  # Devolvemos la probabilidad y el total de intentos

# Ejecutamos ambos métodos
muestras_directas = muestreo_directo(10)  # Generamos 10 muestras directas
print("Muestras directas (R, S):", muestras_directas)  # Imprimimos las muestras directas

prob_r_dado_s, total_intentos = muestreo_por_rechazo(1000)  # Generamos 1000 muestras por rechazo
print(f"P(R=True | S=True) usando muestreo por rechazo: {prob_r_dado_s:.3f} (usando {total_intentos} muestras)")  # Imprimimos el resultado

# Ejemplo de aplicación real: En la simulación de sistemas, el muestreo directo y por rechazo puede ser utilizado para generar muestras de distribuciones complejas, permitiendo el análisis de escenarios y la toma de decisiones.
