# En este ejemplo, eliminamos variables ocultas para calcular una probabilidad marginal
# Usamos una red simple: P(R), P(S | R), P(U | R)

# P(R) - Probabilidad de que llueva
P_R = {
    True: 0.2,  # Probabilidad de que llueva
    False: 0.8  # Probabilidad de que no llueva
}

# P(S | R) - Probabilidad de que el suelo esté mojado dado que llueve o no
P_S_given_R = {
    True: {True: 0.9, False: 0.1},  # P(S=True | R=True), P(S=False | R=True)
    False: {True: 0.2, False: 0.8}  # P(S=True | R=False), P(S=False | R=False)
}

# P(U | R) - Probabilidad de que esté nublado dado que llueve o no
P_U_given_R = {
    True: {True: 0.6, False: 0.4},  # P(U=True | R=True), P(U=False | R=True)
    False: {True: 0.3, False: 0.7}   # P(U=True | R=False), P(U=False | R=False)
}

# Queremos calcular P(S=True | U=True) eliminando la variable oculta R

def eliminacion_variables():
    numerador = 0  # Numerador para P(S=True, U=True)
    total = 0  # Denominador para P(U=True)

    for r in [True, False]:  # Para cada valor de R
        # P(R = r)
        p_r = P_R[r]  # Probabilidad de R

        # P(U = True | R = r)
        p_u_given_r = P_U_given_R[r][True]  # Probabilidad de U dado R

        # P(S = True | R = r)
        p_s_given_r = P_S_given_R[r][True]  # Probabilidad de S dado R

        # Multiplicamos para aplicar la Regla de la Cadena: P(R) * P(U|R) * P(S|R)
        prob = p_r * p_u_given_r * p_s_given_r  # Probabilidad conjunta
        numerador += prob  # Sumamos al numerador

        # También acumulamos el denominador para normalizar
        p_sf_given_r = P_S_given_R[r][False]  # Probabilidad de S=False dado R
        total += p_r * p_u_given_r * (p_s_given_r + p_sf_given_r)  # Probabilidad total

    # Normalizamos
    resultado = numerador / total  # Probabilidad condicional
    return resultado  # Devolvemos el resultado

# Ejecutar el cálculo
resultado = eliminacion_variables()  # Calculamos P(S=True | U=True)
print("P(S=True | U=True):", resultado)  # Imprimimos el resultado

# Ejemplo de aplicación real: En el análisis de datos, la eliminación de variables puede ser utilizada para simplificar modelos complejos, eliminando variables ocultas para calcular probabilidades marginales de manera eficiente.
