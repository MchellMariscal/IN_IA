# Probabilidades de los estados del clima
P_sol = 0.7  # Probabilidad de sol
P_lluvia = 0.3  # Probabilidad de lluvia

# Utilidades para cada decisión y estado del clima
utilidades = {
    'Explorar': {'Sol': 100, 'Lluvia': -50},  # Utilidades para la decisión "Explorar"
    'Quedarse': {'Sol': 20, 'Lluvia': 20}    # Utilidades para la decisión "Quedarse"
}

# Calcular utilidad esperada para cada decisión
for decision in utilidades:  # Para cada decisión
    utilidad = (
        P_sol * utilidades[decision]['Sol'] +  # Utilidad esperada para sol
        P_lluvia * utilidades[decision]['Lluvia']  # Utilidad esperada para lluvia
    )
    print(f"Decisión: {decision}, Utilidad esperada: {utilidad}")  # Imprimimos la decisión y su utilidad esperada

# Ejemplo de aplicación real: En la planificación de actividades al aire libre, las redes de decisión pueden ser utilizadas para evaluar si es mejor realizar una actividad o quedarse en casa, considerando las probabilidades de diferentes condiciones climáticas.
