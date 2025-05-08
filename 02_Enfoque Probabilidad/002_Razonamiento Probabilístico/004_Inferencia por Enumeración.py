# Inferencia por Enumeración en una Red Bayesiana simple

# Definimos las probabilidades de la red bayesiana manualmente
# Suponemos una red muy simple: P(R) y P(S | R)

# P(R) - Probabilidad de que llueva
P_R = {
    True: 0.2,  # Probabilidad de que llueva
    False: 0.8  # Probabilidad de que no llueva
}

# P(S | R) - Probabilidad de que el césped esté mojado dado que llueve o no
P_S_given_R = {
    True: {True: 0.9, False: 0.1},   # P(S=True | R=True), P(S=False | R=True)
    False: {True: 0.2, False: 0.8}   # P(S=True | R=False), P(S=False | R=False)
}

# Función de inferencia por enumeración: P(R | S=True)
def enumeracion_inversa():
    numerador = {}  # Diccionario para el numerador
    total = 0  # Total para normalizar

    for r_val in [True, False]:  # Para cada valor de R
        # P(R = r_val)
        p_r = P_R[r_val]  # Probabilidad de R

        # P(S = True | R = r_val)
        p_s_given_r = P_S_given_R[r_val][True]  # Probabilidad de S dado R

        # Multiplicamos las probabilidades (regla de la cadena)
        conjunto = p_r * p_s_given_r  # P(R) * P(S|R)

        numerador[r_val] = conjunto  # Guardamos el conjunto
        total += conjunto  # Sumamos al total

    # Normalizamos
    for val in numerador:  # Para cada valor en el numerador
        numerador[val] /= total  # Normalizamos

    return numerador  # Devolvemos el numerador normalizado

# Ejecutamos la inferencia
resultado = enumeracion_inversa()  # Calculamos P(R | S=True)
print("P(R | S=True):", resultado)  # Imprimimos el resultado

# Ejemplo de aplicación real: En el diagnóstico médico, la inferencia por enumeración puede ser utilizada para calcular la probabilidad de una enfermedad dado un síntoma, considerando todas las posibles combinaciones de factores.
