def decision_lluvia(prob_lluvia, valor_paraguas=1, costo_mojarse=5):
    # Definimos un modelo probabilista racional para decidir si llevar paraguas
    utilidad_llevar = -valor_paraguas  # Utilidad de llevar paraguas
    utilidad_no_llevar = -prob_lluvia * costo_mojarse  # Utilidad de no llevar paraguas
    if utilidad_llevar > utilidad_no_llevar:  # Si la utilidad de llevar es mayor
        return "No llevar paraguas"  # Devolvemos que no llevar paraguas
    return "Llevar paraguas"  # Devolvemos que llevar paraguas

print(decision_lluvia(0.6))  # Imprimimos la decisión para una probabilidad de lluvia de 0.6
print(decision_lluvia(0.9))  # Imprimimos la decisión para una probabilidad de lluvia de 0.9

# Ejemplo de aplicación real: En la toma de decisiones, los modelos probabilistas racionales pueden ser utilizados para evaluar acciones basadas en probabilidades y utilidades, considerando los costos y beneficios.
