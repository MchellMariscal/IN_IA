# En este ejemplo, eliminamos variables ocultas para calcular una probabilidad marginal
# Usamos una red simple: P(R), P(S | R), P(U | R)

# P(R) - Probabilidad de que llueva
P_R = {
    True: 0.2,
    False: 0.8
}

# P(S | R) - Probabilidad de que el suelo esté mojado dado que llueva
P_S_given_R = {
    True: {True: 0.9, False: 0.1},
    False: {True: 0.2, False: 0.8}
}

# P(U | R) - Probabilidad de que esté nublado dado que llueva
P_U_given_R = {
    True: {True: 0.6, False: 0.4},
    False: {True: 0.3, False: 0.7}
}

# Queremos calcular P(S=True | U=True) eliminando la variable oculta R

def eliminacion_variables():
    numerador = 0
    total = 0

    for r in [True, False]:
        # P(R = r)
        p_r = P_R[r]

        # P(U = True | R = r)
        p_u_given_r = P_U_given_R[r][True]

        # P(S = True | R = r)
        p_s_given_r = P_S_given_R[r][True]

        # Multiplicamos para aplicar la Regla de la Cadena: P(R) * P(U|R) * P(S|R)
        prob = p_r * p_u_given_r * p_s_given_r
        numerador += prob

        # También acumulamos el denominador para normalizar
        p_sf_given_r = P_S_given_R[r][False]
        total += p_r * p_u_given_r * (p_s_given_r + p_sf_given_r)

    # Normalizamos
    resultado = numerador / total
    return resultado

# Ejecutar el cálculo
resultado = eliminacion_variables()
print("P(S=True | U=True):", resultado)
