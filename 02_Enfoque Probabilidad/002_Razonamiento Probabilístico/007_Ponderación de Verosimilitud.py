import random

# Definimos la red bayesiana
P_R = {
    True: 0.2,
    False: 0.8
}

P_S_given_R = {
    True: {True: 0.9, False: 0.1},
    False: {True: 0.2, False: 0.8}
}

# La variable observada es S = True

# Función de muestreo con ponderación por verosimilitud
def ponderacion_verosimilitud(n):
    pesos = []
    muestras_r = []

    for _ in range(n):
        r = random.choices([True, False], weights=[P_R[True], P_R[False]])[0]

        # Asumimos evidencia S=True y ponderamos con su verosimilitud P(S=True | R)
        peso = P_S_given_R[r][True]

        muestras_r.append(r)
        pesos.append(weso)

    total_peso = sum(pesos)
    if total_peso == 0:
        return 0
    
    prob_r_true = sum(w for r, w in zip(muestras_r, pesos) if r) / total_peso
    return prob_r_true

# Ejecutamos la estimación
probabilidad_estimacion = ponderacion_verosimilitud(1000)
print(f"P(R=True | S=True) usando ponderación de verosimilitud: {probabilidad_estimacion:.3f}")
