# Definimos las acciones y sus resultados posibles
acciones = {
    'Explorar': [
        {'prob': 0.6, 'utilidad': 100},
        {'prob': 0.4, 'utilidad': -50}
    ],
    'Base': [
        {'prob': 1.0, 'utilidad': 20}
    ]
}

# Calculamos utilidad esperada para cada acción
def utilidad_esperada(accion):
    return sum(resultado['prob'] * resultado['utilidad'] for resultado in accion)

for nombre, resultados in acciones.items():
    utilidad = utilidad_esperada(resultados)
    print(f"Acción: {nombre}, Utilidad esperada: {utilidad}")
