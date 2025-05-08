# Encadenamiento hacia atrás para probar un objetivo
def encadenamiento_atras(objetivo, reglas, hechos):
    if objetivo in hechos:  # Si el objetivo es un hecho conocido
        return True  # El objetivo es verdadero
    for antecedente, consecuente in reglas:  # Para cada regla
        if consecuente == objetivo and encadenamiento_atras(antecedente, reglas, hechos):  # Si el consecuente es el objetivo y el antecedente es verdadero
            return True  # El objetivo es verdadero
    return False  # El objetivo es falso

hechos = {"llueve"}  # Hechos conocidos
reglas = [("llueve", "suelo_mojado")]  # Reglas de inferencia

print("¿Se puede probar 'suelo_mojado'?", encadenamiento_atras("suelo_mojado", reglas, hechos))  # Imprimimos el resultado del encadenamiento

# Ejemplo de aplicación real: En los sistemas expertos, el encadenamiento hacia atrás puede ser utilizado para probar hipótesis a partir de reglas y hechos conocidos, considerando la aplicación de reglas de inferencia.

