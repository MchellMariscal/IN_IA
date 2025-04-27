def filtrado(observaciones, belief, transicion, sensor):
    for obs in observaciones:
        new_belief = {}
        for estado in belief:
            total = 0
            for prev_estado in belief:
                total += transicion[prev_estado].get(estado, 0) * belief[prev_estado]
            new_belief[estado] = sensor[estado].get(obs, 0) * total
        # Normalizar
        normalizador = sum(new_belief.values())
        for estado in new_belief:
            new_belief[estado] /= normalizador
        belief = new_belief
    return belief

filtrado_resultado = filtrado(observaciones, belief, transicion, sensor)
print("Resultado de filtrado (belief final):")
print(filtrado_resultado)
