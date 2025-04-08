import random

# Estados posibles
estados = ['bueno', 'malo']

# Acciones posibles
acciones = ['esperar', 'actuar']

# Observaciones posibles
observaciones = ['positivo', 'negativo']

# Matriz de observación: P(o | s)
observacion = {
    'bueno': {'positivo': 0.8, 'negativo': 0.2},
    'malo':  {'positivo': 0.3, 'negativo': 0.7}
}

# Recompensas
def recompensa(estado, accion):
    if accion == 'actuar':
        return 10 if estado == 'bueno' else -10
    else:
        return -1  # penalización por esperar

# Transición (estado no cambia para simplificar)
def transicion(estado, accion):
    return estado

# Observación aleatoria
def generar_observacion(estado):
    probs = observacion[estado]
    return random.choices(list(probs.keys()), weights=probs.values())[0]

# Actualización de creencia (bayesiana)
def actualizar_creencia(belief, accion, observacion_recibida):
    nueva_creencia = {}
    total = 0
    for estado in estados:
        prob_o_dado_s = observacion[estado][observacion_recibida]
        nueva_creencia[estado] = belief[estado] * prob_o_dado_s
        total += nueva_creencia[estado]
    # Normalizar
    for estado in estados:
        nueva_creencia[estado] /= total
    return nueva_creencia

# Creencia inicial (uniforme)
belief = {'bueno': 0.5, 'malo': 0.5}

# Simulación de pasos
estado_real = random.choice(estados)
print(f"Estado real (oculto): {estado_real}\n")

for paso in range(5):
    print(f"Paso {paso + 1}")
    print(f"Creencia: {belief}")

    # Decidir acción según creencia
    if belief['bueno'] > 0.7:
        accion = 'actuar'
    else:
        accion = 'esperar'

    obs = generar_observacion(estado_real)
    r = recompensa(estado_real, accion)
    print(f"Acción: {accion}, Observación: {obs}, Recompensa: {r}")

    # Actualizar creencia
    belief = actualizar_creencia(belief, accion, obs)

    print("----\n")
