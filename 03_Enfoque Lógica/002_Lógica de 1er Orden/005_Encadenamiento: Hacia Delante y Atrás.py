# Encadenamiento hacia atrás para probar un objetivo
def encadenamiento_atras(objetivo, reglas, hechos):
    if objetivo in hechos:
        return True
    for antecedente, consecuente in reglas:
        if consecuente == objetivo and encadenamiento_atras(antecedente, reglas, hechos):
            return True
    return False

hechos = {"llueve"}
reglas = [("llueve", "suelo_mojado")]

print("¿Se puede probar 'suelo_mojado'?", encadenamiento_atras("suelo_mojado", reglas, hechos))
