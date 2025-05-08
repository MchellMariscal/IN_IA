import random

# Estados posibles
estados = ['bueno', 'malo']

# Acciones posibles
acciones = ['esperar', 'actuar']

# Observaciones posibles
observaciones = ['positivo', 'negativo']

# Matriz de observación: P(o | s)
observacion = {
    'bueno': {'positivo': 0.8, 'negativo': 0.2},  # Probabilidades de observación para el estado "bueno"
    'malo':  {'positivo': 0.3, 'negativo': 0.7}   # Probabilidades de observación para el estado "malo"
}

# Recompensas
def recompensa(estado, accion):
    if accion == 'actuar':  # Si la acción es "actuar"
        return 10 if estado == 'bueno' else -10  # Recompensa según el estado
    else:
        return -1  # penalización por esperar

# Transición (estado no cambia para simplificar)
def transicion(estado, accion):
    return estado  # El estado no cambia

# Observación aleatoria
def generar_observacion(estado):
    probs = observacion[estado]  # Probabilidades de observación
    return random.choices(list(probs.keys()), weights=probs.values())[0]  # Generamos una observación aleatoria

# Actualización de creencia (bayesiana)
def actualizar_creencia(belief, accion, observacion_recibida):
    nueva_creencia = {}  # Nueva creencia
    total = 0  # Total para normalizar
    for estado in estados:  # Para cada estado
        prob_o_dado_s = observacion[estado][observacion_recibida]  # Probabilidad de la observación dado el estado
        nueva_creencia[estado] = belief[estado] * prob_o_dado_s  # Actualizamos la creencia
        total += nueva_creencia[estado]  # Actualizamos el total
    # Normalizar
    for estado in estados:  # Para cada estado
        nueva_creencia[estado] /= total  # Normalizamos la creencia
    return nueva_creencia  # Devolvemos la nueva creencia

# Creencia inicial (uniforme)
belief = {'bueno': 0.5, 'malo': 0.5}  # Creencia inicial

# Simulación de pasos
estado_real = random.choice(estados)  # Estado real (oculto)
print(f"Estado real (oculto): {estado_real}\n")  # Imprimimos el estado real

for paso in range(5):  # Para cada paso
    print(f"Paso {paso + 1}")  # Imprimimos el paso
    print(f"Creencia: {belief}")  # Imprimimos la creencia

    # Decidir acción según creencia
    if belief['bueno'] > 0.7:  # Si la creencia en "bueno" es mayor que 0.7
        accion = 'actuar'  # Acción "actuar"
    else:
        accion = 'esperar'  # Acción "esperar"

    obs = generar_observacion(estado_real)  # Generamos una observación
    r = recompensa(estado_real, accion)  # Calculamos la recompensa
    print(f"Acción: {accion}, Observación: {obs}, Recompensa: {r}")  # Imprimimos la acción, observación y recompensa

    # Actualizar creencia
    belief = actualizar_creencia(belief, accion, obs)  # Actualizamos la creencia

    print("----\n")  # Separador

# Ejemplo de aplicación real: En la robótica, los MDP parcialmente observables pueden ser utilizados para tomar decisiones en entornos con incertidumbre, donde el estado completo no es conocido, como en la navegación en entornos desconocidos.
