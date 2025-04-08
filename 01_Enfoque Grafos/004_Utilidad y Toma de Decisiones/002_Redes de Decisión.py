# Probabilidades
P_sol = 0.7
P_lluvia = 0.3

# Utilidades
utilidades = {
    'Explorar': {'Sol': 100, 'Lluvia': -50},
    'Quedarse': {'Sol': 20, 'Lluvia': 20}
}

# Calcular utilidad esperada para cada decisión
for decision in utilidades:
    utilidad = (
        P_sol * utilidades[decision]['Sol'] +
        P_lluvia * utilidades[decision]['Lluvia']
    )
    print(f"Decisión: {decision}, Utilidad esperada: {utilidad}")
