# Definimos las acciones y sus resultados posibles
acciones = {
    'Explorar': [
        {'prob': 0.6, 'utilidad': 100},  # Resultado 1: probabilidad 0.6, utilidad 100
        {'prob': 0.4, 'utilidad': -50}   # Resultado 2: probabilidad 0.4, utilidad -50
    ],
    'Base': [
        {'prob': 1.0, 'utilidad': 20}    # Resultado único: probabilidad 1.0, utilidad 20
    ]
}

# Calculamos utilidad esperada para cada acción
def utilidad_esperada(accion):
    return sum(resultado['prob'] * resultado['utilidad'] for resultado in accion)  # Suma de probabilidad * utilidad para cada resultado

for nombre, resultados in acciones.items():  # Para cada acción
    utilidad = utilidad_esperada(resultados)  # Calculamos la utilidad esperada
    print(f"Acción: {nombre}, Utilidad esperada: {utilidad}")  # Imprimimos la acción y su utilidad esperada

# Ejemplo de aplicación real: En la toma de decisiones financieras, la teoría de la utilidad puede ser utilizada para evaluar diferentes opciones de inversión, considerando tanto los posibles rendimientos como los riesgos asociados.
