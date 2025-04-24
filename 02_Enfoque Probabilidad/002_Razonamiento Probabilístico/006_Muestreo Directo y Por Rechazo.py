import random

# Definimos las distribuciones condicionales para una red bayesiana simple
# P(R) - Probabilidad de que llueva
P_R = {
    True: 0.2,
    False: 0.8
}

# P(S | R) - Probabilidad de que el suelo esté mojado dado que llueve o no
P_S_given_R = {
    True: {True: 0.9, False: 0.1},
    False: {True: 0.2, False: 0.8}
}

# Muestreo Directo: genera muestras de R y S directamente desde la red

def muestreo_directo(n):
    muestras = []
    for _ in range(n):
        r = random.choices([True, False], weights=[P_R[True], P_R[False]])[0]
        s = random.choices([True, False], weights=[P_S_given_R[r][True], P_S_given_R[r][False]])[0]
        muestras.append((r, s))
    return muestras

# Muestreo por Rechazo: sólo acepta muestras que coincidan con la evidencia S=True

def muestreo_por_rechazo(n):
    aceptadas = []
    total = 0
    while len(aceptadas) < n:
        r = random.choices([True, False], weights=[P_R[True], P_R[False]])[0]
        s = random.choices([True, False], weights=[P_S_given_R[r][True], P_S_given_R[r][False]])[0]
        total += 1
        if s is True:
            aceptadas.append(r)
    prob_lluvia_dado_s = aceptadas.count(True) / len(aceptadas)
    return prob_lluvia_dado_s, total

# Ejecutamos ambos métodos
muestras_directas = muestreo_directo(10)
print("Muestras directas (R, S):", muestras_directas)

prob_r_dado_s, total_intentos = muestreo_por_rechazo(1000)
print(f"P(R=True | S=True) usando muestreo por rechazo: {prob_r_dado_s:.3f} (usando {total_intentos} muestras)")