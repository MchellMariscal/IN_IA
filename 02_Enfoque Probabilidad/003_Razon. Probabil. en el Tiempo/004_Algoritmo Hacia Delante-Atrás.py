# Función para realizar el filtrado
def filtrado(observaciones, belief, transicion, sensor):
    for obs in observaciones:  # Para cada observación
        new_belief = {}  # Nueva creencia
        for estado in belief:  # Para cada estado
            total = 0  # Total para normalizar
            for prev_estado in belief:  # Para cada estado previo
                total += transicion[prev_estado].get(estado, 0) * belief[prev_estado]  # Actualizamos el total
            new_belief[estado] = sensor[estado].get(obs, 0) * total  # Actualizamos la creencia
        # Normalizar
        normalizador = sum(new_belief.values())  # Calculamos el normalizador
        for estado in new_belief:  # Para cada estado
            new_belief[estado] /= normalizador  # Normalizamos
        belief = new_belief  # Actualizamos la creencia
    return belief  # Devolvemos la creencia

filtrado_resultado = filtrado(observaciones, belief, transicion, sensor)  # Realizamos el filtrado
print("Resultado de filtrado (belief final):")  # Imprimimos el resultado del filtrado
print(filtrado_resultado)  # Imprimimos la creencia final

# Ejemplo de aplicación real: En la navegación autónoma, el algoritmo hacia adelante-atrás puede ser utilizado para estimar la posición de un vehículo, considerando las observaciones y las transiciones entre estados.
