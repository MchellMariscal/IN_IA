# Inferencia por Enumeración en una Red Bayesiana simple
# NOTA: Esta práctica está comentada paso a paso

# Definimos las probabilidades de la red bayesiana manualmente
# Suponemos una red muy simple: P(R) y P(S | R)

# P(R) - Probabilidad de que llueva
P_R = {
    True: 0.2,
    False: 0.8
}

# P(S | R) - Probabilidad de que el césped esté mojado dado que llueve o no
P_S_given_R = {
    True: {True: 0.9, False: 0.1},   # P(S=True | R=True), P(S=False | R=True)
    False: {True: 0.2, False: 0.8}   # P(S=True | R=False), P(S=False | R=False)
}

# Función de inferencia por enumeración: P(R | S=True)
def enumeracion_inversa():
    numerador = {}
    total = 0

    for r_val in [True, False]:
        # P(R = r_val)
        p_r = P_R[r_val]

        # P(S = True | R = r_val)
        p_s_given_r = P_S_given_R[r_val][True]

        # Multiplicamos las probabilidades (regla de la cadena)
        conjunto = p_r * p_s_given_r

        numerador[r_val] = conjunto
        total += conjunto

    # Normalizamos
    for val in numerador:
        numerador[val] /= total

    return numerador

# Ejecutamos la inferencia
resultado = enumeracion_inversa()
print("P(R | S=True):", resultado)
